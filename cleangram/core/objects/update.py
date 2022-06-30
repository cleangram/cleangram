from __future__ import annotations

import abc
from functools import lru_cache
from typing import TYPE_CHECKING, Optional, Tuple

from ..bot.bot import Bot
from .base import TelegramObject

if TYPE_CHECKING:
    from .callback_query import CallbackQuery
    from .chat_join_request import ChatJoinRequest
    from .chat_member_updated import ChatMemberUpdated
    from .chosen_inline_result import ChosenInlineResult
    from .inline_query import InlineQuery
    from .message import Message
    from .poll import Poll
    from .poll_answer import PollAnswer
    from .pre_checkout_query import PreCheckoutQuery
    from .shipping_query import ShippingQuery


class Update(TelegramObject, abc.ABC):
    """
    This object represents an incoming update.At most one of the optional
    parameters can be present in any given update.

    Reference: https://core.telegram.org/bots/api#update
    """

    update_id: int
    """The update's unique identifier. Update identifiers start from a
    certain positive number and increase sequentially. This ID becomes
    especially handy if you're using webhooks, since it allows you to
    ignore repeated updates or to restore the correct update sequence,
    should they get out of order. If there are no new updates for at least
    a week, then identifier of the next update will be chosen randomly
    instead of sequentially."""

    message: Optional[Message] = None
    """Optional. New incoming message of any kind - text, photo, sticker,
    etc."""

    edited_message: Optional[Message] = None
    """Optional. New version of a message that is known to the bot and was
    edited"""

    channel_post: Optional[Message] = None
    """Optional. New incoming channel post of any kind - text, photo,
    sticker, etc."""

    edited_channel_post: Optional[Message] = None
    """Optional. New version of a channel post that is known to the bot and
    was edited"""

    inline_query: Optional[InlineQuery] = None
    """Optional. New incoming inline query"""

    chosen_inline_result: Optional[ChosenInlineResult] = None
    """Optional. The result of an inline query that was chosen by a user and
    sent to their chat partner. Please see our documentation on the
    feedback collecting for details on how to enable these updates for
    your bot."""

    callback_query: Optional[CallbackQuery] = None
    """Optional. New incoming callback query"""

    shipping_query: Optional[ShippingQuery] = None
    """Optional. New incoming shipping query. Only for invoices with flexible
    price"""

    pre_checkout_query: Optional[PreCheckoutQuery] = None
    """Optional. New incoming pre-checkout query. Contains full information
    about checkout"""

    poll: Optional[Poll] = None
    """Optional. New poll state. Bots receive only updates about stopped
    polls and polls, which are sent by the bot"""

    poll_answer: Optional[PollAnswer] = None
    """Optional. A user changed their answer in a non-anonymous poll. Bots
    receive new votes only in polls that were sent by the bot itself."""

    my_chat_member: Optional[ChatMemberUpdated] = None
    """Optional. The bot's chat member status was updated in a chat. For
    private chats, this update is received only when the bot is blocked or
    unblocked by the user."""

    chat_member: Optional[ChatMemberUpdated] = None
    """Optional. A chat member's status was updated in a chat. The bot must
    be an administrator in the chat and must explicitly specify
    “chat_member” in the list of allowed_updates to receive these updates."""

    chat_join_request: Optional[ChatJoinRequest] = None
    """Optional. A request to join the chat has been sent. The bot must have
    the can_invite_users administrator right in the chat to receive these
    updates."""

    def adjust(self, bot: Bot):
        self.event.adjust(bot)

    def __hash__(self):
        return hash(self.update_id)

    @lru_cache()
    def get_event_type(self) -> Tuple[TelegramObject, str]:
        if self.message:
            return self.message, 'message'
        if self.edited_message:
            return self.edited_message, 'edited_message'
        if self.channel_post:
            return self.channel_post, 'channel_post'
        if self.edited_channel_post:
            return self.edited_channel_post, 'edited_channel_post'
        if self.inline_query:
            return self.inline_query, 'inline_query'
        if self.chosen_inline_result:
            return self.chosen_inline_result, 'chosen_inline_result'
        if self.callback_query:
            return self.callback_query, 'callback_query'
        if self.shipping_query:
            return self.shipping_query, 'shipping_query'
        if self.pre_checkout_query:
            return self.pre_checkout_query, 'pre_checkout_query'
        if self.poll:
            return self.poll, 'poll'
        if self.poll_answer:
            return self.poll_answer, 'poll_answer'
        if self.my_chat_member:
            return self.my_chat_member, 'my_chat_member'
        if self.chat_member:
            return self.chat_member, 'chat_member'
        if self.chat_join_request:
            return self.chat_join_request, 'chat_join_request'
        raise NameError("Event Not Found")

    @property
    def event(self) -> TelegramObject:
        return self.event_type[0]

    event_type = property(get_event_type)
