from __future__ import annotations

import contextlib
from time import time
from typing import Any, Generator, List, Set, Union, overload, Sequence, Optional, Dict

from .observers.manager import ContextManagerObserver
from .utils import check_filters
from ...base import TelegramType
from ...base.app.blueprint import BaseBlueprint
from ...base.app.observers import BaseHandlerObserver
from ...utils.event_type import get_event_and_type
from ..client.bot import Bot
from ..methods import TelegramMethod
from ..types import (CallbackQuery, ChatJoinRequest, ChatMemberUpdated,
                     ChosenInlineResult, InlineQuery, Message, Poll,
                     PollAnswer, PreCheckoutQuery, ShippingQuery, Update)
from .observers.event import EventObserver
from .observers.handler import HandlerObserver


class Blueprint(BaseBlueprint):
    def __init__(
        self,
        name: str = "bp",
        *filters,
        **kwargs
    ) -> None:
        self.message = HandlerObserver(self, Message)
        self.edited_message = HandlerObserver(self, Message)
        self.channel_post = HandlerObserver(self, Message)
        self.edited_channel_post = HandlerObserver(self, Message)
        self.inline_query = HandlerObserver(self, InlineQuery)
        self.chosen_inline_result = HandlerObserver(self, ChosenInlineResult)
        self.callback_query = HandlerObserver(self, CallbackQuery)
        self.shipping_query = HandlerObserver(self, ShippingQuery)
        self.pre_checkout_query = HandlerObserver(self, PreCheckoutQuery)
        self.poll = HandlerObserver(self, Poll)
        self.poll_answer = HandlerObserver(self, PollAnswer)
        self.my_chat_member = HandlerObserver(self, ChatMemberUpdated)
        self.chat_member = HandlerObserver(self, ChatMemberUpdated)
        self.chat_join_request = HandlerObserver(self, ChatJoinRequest)

        self.setup = EventObserver(self)
        self.startup = EventObserver(self)
        self.middleware = ContextManagerObserver()
        self.shutdown = EventObserver(self)
        self.destroy = EventObserver(self)

        super().__init__(name, *filters, **kwargs)

    async def run_setup(self):
        await self.setup.notify()
        for st in self._children:
            await st.run_setup()

    async def run_startup(self, **kwargs):
        if deps := await self.startup.notify(**kwargs):
            if isinstance(deps, dict):
                self._deps.update(deps)
        for bp in self._children:
            await bp.run_startup(**self._deps, **kwargs)

    async def _notify(self, update: Update, event: TelegramType, type_: str, **kwargs):
        if (f_kwargs := await check_filters(update, self._filters, **kwargs)) is not None:
            async with self.middleware.notify(update=update, **kwargs, **f_kwargs) as mw_kwargs:
                if processed := await self._handler_observers[type_].notify(
                    event, **kwargs, **f_kwargs, **mw_kwargs
                ):
                    return processed
                else:
                    for bp in self._children:
                        if processed := await bp._notify(
                            update, event, type_, **kwargs, **f_kwargs, **mw_kwargs
                        ):
                            return processed

    async def run_destroy(self):
        await self.destroy.notify()
        for dt in self._children:
            await dt.run_destroy()

    async def run_shutdown(self, **kwargs):
        await self.shutdown.notify(bp=self, **self._deps, **kwargs)
        for bp in self._children:
            await bp.run_shutdown()
