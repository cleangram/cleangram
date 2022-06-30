from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...core import Update as _Update

if TYPE_CHECKING:
    from .callback_query import CallbackQuery
    from .chat_join_request import ChatJoinRequest
    from .chat_member_updated import ChatMemberUpdated
    from .message import Message


class Update(_Update):
    """
    This object represents an incoming update.At most one of the optional
    parameters can be present in any given update.

    Reference: https://core.telegram.org/bots/api#update
    """

    message: Optional[Message] = None
    edited_message: Optional[Message] = None
    channel_post: Optional[Message] = None
    edited_channel_post: Optional[Message] = None
    callback_query: Optional[CallbackQuery] = None
    my_chat_member: Optional[ChatMemberUpdated] = None
    chat_member: Optional[ChatMemberUpdated] = None
    chat_join_request: Optional[ChatJoinRequest] = None
