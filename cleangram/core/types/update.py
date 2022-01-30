from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .chosen_inline_result import ChosenInlineResult
from .shipping_query import ShippingQuery
from .inline_query import InlineQuery
from .pre_checkout_query import PreCheckoutQuery
from .poll import Poll
from .poll_answer import PollAnswer
from .chat_join_request import ChatJoinRequest
from .base import TelegramType
from .callback_query import CallbackQuery
from .chat_member_updated import ChatMemberUpdated
from .message import Message


@dataclass
class Update(TelegramType):
    """
    This object represents an incoming update.At most one of the
    optional parameters can be present in any given update.
    Reference: https://core.telegram.org/bots/api#update
    """

    update_id: int
    """The update's unique identifier. Update identifiers start
    from a certain positive number and increase sequentially.
    This ID becomes especially handy if you're using Webhooks,
    since it allows you to ignore repeated updates or to restore
    the correct update sequence, should they get out of order.
    If there are no new updates for at least a week, then
    identifier of the next update will be chosen randomly
    instead of sequentially."""

    message: Optional[Message] = field(default=None)
    """Optional. New incoming message of any kind — text, photo,
    sticker, etc."""

    edited_message: Optional[Message] = field(default=None)
    """Optional. New version of a message that is known to the bot
    and was edited"""

    channel_post: Optional[Message] = field(default=None)
    """Optional. New incoming channel post of any kind — text,
    photo, sticker, etc."""

    edited_channel_post: Optional[Message] = field(default=None)
    """Optional. New version of a channel post that is known to the
    bot and was edited"""

    inline_query: Optional[InlineQuery] = field(default=None)
    """Optional. New incoming inline query"""

    chosen_inline_result: Optional[ChosenInlineResult] = field(default=None)
    """Optional. The result of an inline query that was chosen by a
    user and sent to their chat partner. Please see our
    documentation on the feedback collecting for details on how
    to enable these updates for your bot."""

    callback_query: Optional[CallbackQuery] = field(default=None)
    """Optional. New incoming callback query"""

    shipping_query: Optional[ShippingQuery] = field(default=None)
    """Optional. New incoming shipping query. Only for invoices
    with flexible price"""

    pre_checkout_query: Optional[PreCheckoutQuery] = field(default=None)
    """Optional. New incoming pre-checkout query. Contains full
    information about checkout"""

    poll: Optional[Poll] = field(default=None)
    """Optional. New poll state. Bots receive only updates about
    stopped polls and polls, which are sent by the bot"""

    poll_answer: Optional[PollAnswer] = field(default=None)
    """Optional. A user changed their answer in a non-anonymous
    poll. Bots receive new votes only in polls that were sent by
    the bot itself."""

    my_chat_member: Optional[ChatMemberUpdated] = field(default=None)
    """Optional. The bot's chat member status was updated in a
    chat. For private chats, this update is received only when
    the bot is blocked or unblocked by the user."""

    chat_member: Optional[ChatMemberUpdated] = field(default=None)
    """Optional. A chat member's status was updated in a chat. The
    bot must be an administrator in the chat and must explicitly
    specify “chat_member” in the list of allowed_updates to
    receive these updates."""

    chat_join_request: Optional[ChatJoinRequest] = field(default=None)
    """Optional. A request to join the chat has been sent. The bot
    must have the can_invite_users administrator right in the
    chat to receive these updates."""
