from __future__ import annotations

import contextlib

from typing import List, Any, Union, Set, Generator

from .observers.event import EventObserver
from .observers.handler import HandlerObserver
from ..types import (
    Message,
    Update,
    InlineQuery,
    ChosenInlineResult,
    CallbackQuery,
    PreCheckoutQuery,
    ShippingQuery,
    Poll,
    PollAnswer,
    ChatMemberUpdated,
    ChatJoinRequest,
)
from ..methods import TelegramMethod
from ..client.bot import Bot
from ...utils.event_type import get_event_and_type


class Blueprint:
    def __init__(
        self,
        *args: Any,
        blueprints: List[Blueprint] = (),
        middlewares: List = (),
        **kwargs: Any,
    ) -> None:
        self.__blueprints: List[Blueprint] = [self, *blueprints]
        self.__middlewares = [*middlewares]

        self.message = HandlerObserver[Message]()
        self.edited_message = HandlerObserver[Message]()
        self.channel_post = HandlerObserver[Message]()
        self.edited_channel_post = HandlerObserver[Message]()
        self.inline_query = HandlerObserver[InlineQuery]()
        self.chosen_inline_result = HandlerObserver[ChosenInlineResult]()
        self.callback_query = HandlerObserver[CallbackQuery]()
        self.shipping_query = HandlerObserver[ShippingQuery]()
        self.pre_checkout_query = HandlerObserver[PreCheckoutQuery]()
        self.poll = HandlerObserver[Poll]()
        self.poll_answer = HandlerObserver[PollAnswer]()
        self.my_chat_member = HandlerObserver[ChatMemberUpdated]()
        self.chat_member = HandlerObserver[ChatMemberUpdated]()
        self.chat_join_request = HandlerObserver[ChatJoinRequest]()

        self.startup = EventObserver()
        self.shutdown = EventObserver()

        self.__handler_observers = {
            "message": self.message,
            "edited_message": self.edited_message,
            "channel_post": self.channel_post,
            "edited_channel_post": self.edited_channel_post,
            "inline_query": self.inline_query,
            "chosen_inline_result": self.chosen_inline_result,
            "callback_query": self.callback_query,
            "shipping_query": self.shipping_query,
            "pre_checkout_query": self.pre_checkout_query,
            "poll": self.poll,
            "poll_answer": self.poll_answer,
            "my_chat_member": self.my_chat_member,
            "chat_member": self.chat_member,
            "chat_join_request": self.chat_join_request,
        }

    async def notify(
        self, update: Update, bot: Bot
    ) -> Union[TelegramMethod, bool, None]:
        async with contextlib.AsyncExitStack() as stack:
            mds = [await stack.enter_async_context(md()) for md in self.__middlewares]
            event, event_type = get_event_and_type(update)
            for router in self.__blueprints:
                if method := await router.__handler_observers[event_type].notify(
                    event, bot, mds
                ):
                    return method
        return True

    async def emit_startup(self):
        await self.startup.notify()
        for bp in self.__blueprints[1:]:
            await bp.emit_startup()

    async def emit_shutdown(self):
        await self.shutdown.notify()
        for bp in self.__blueprints[1:]:
            await bp.emit_shutdown()

    def middleware(self, gen):
        self.__middlewares.append(contextlib.asynccontextmanager(gen))
        return gen
