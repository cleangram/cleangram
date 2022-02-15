from __future__ import annotations

from typing import Optional, List, Union, Dict

from .observers.event import EventsObserver
from ..client import Bot
from ..methods import TelegramMethod
from ..types import Message, Update, InlineQuery, ChosenInlineResult, CallbackQuery, ShippingQuery, PreCheckoutQuery, \
    Poll, PollAnswer, ChatMemberUpdated, ChatJoinRequest, TelegramType
from .observers.update import HandlerObserver
from ..utils.update_event import get_event_and_type


class Blueprint:
    def __init__(
        self,
        blueprints: List[Blueprint] = None,
        **kwargs
    ):
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

        self.startup = EventsObserver()
        self.shutdown = EventsObserver()

        self.__blueprints: List[Blueprint] = [self] + (blueprints or [])
        self.__updates_observer: Dict[str, HandlerObserver] = {
            "message": self.message,
            "edited_message": self.edited_message
        }

    async def notify(self, update: Update, bot: Bot) -> Union[TelegramMethod, bool, None]:
        event, event_type = get_event_and_type(update)
        for router in self.__blueprints:
            if method := await router.__updates_observer[event_type].notify(event, bot):
                return method

    async def include(self, blueprint: Blueprint):
        self.__blueprints.append(blueprint)

    async def exclude(self, blueprint: Blueprint):
        self.__blueprints.remove(blueprint)
