from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Optional

from ..bot.bot import Bot
from .base import TelegramObject

if TYPE_CHECKING:
    from .chat_location import ChatLocation
    from .chat_permissions import ChatPermissions
    from .chat_photo import ChatPhoto
    from .message import Message


class Chat(TelegramObject, abc.ABC):
    """
    This object represents a chat.

    Reference: https://core.telegram.org/bots/api#chat
    """

    id: int
    """Unique identifier for this chat. This number may have more than 32
    significant bits and some programming languages may have
    difficulty/silent defects in interpreting it. But it has at most 52
    significant bits, so a signed 64-bit integer or double-precision float
    type are safe for storing this identifier."""

    type: str
    """Type of chat, can be either “private”, “group”, “supergroup” or
    “channel”"""

    title: Optional[str] = None
    """Optional. Title, for supergroups, channels and group chats"""

    username: Optional[str] = None
    """Optional. Username, for private chats, supergroups and channels if
    available"""

    first_name: Optional[str] = None
    """Optional. First name of the other party in a private chat"""

    last_name: Optional[str] = None
    """Optional. Last name of the other party in a private chat"""

    photo: Optional[ChatPhoto] = None
    """Optional. Chat photo. Returned only in getChat."""

    bio: Optional[str] = None
    """Optional. Bio of the other party in a private chat. Returned only in
    getChat."""

    has_private_forwards: Optional[bool] = None
    """Optional. True, if privacy settings of the other party in the private
    chat allows to use tg://user?id=<user_id> links only in chats with the
    user. Returned only in getChat."""

    join_to_send_messages: Optional[bool] = None
    """Optional. True, if users need to join the supergroup before they can
    send messages. Returned only in getChat."""

    join_by_request: Optional[bool] = None
    """Optional. True, if all users directly joining the supergroup need to
    be approved by supergroup administrators. Returned only in getChat."""

    description: Optional[str] = None
    """Optional. Description, for groups, supergroups and channel chats.
    Returned only in getChat."""

    invite_link: Optional[str] = None
    """Optional. Primary invite link, for groups, supergroups and channel
    chats. Returned only in getChat."""

    pinned_message: Optional[Message] = None
    """Optional. The most recent pinned message (by sending date). Returned
    only in getChat."""

    permissions: Optional[ChatPermissions] = None
    """Optional. Default chat member permissions, for groups and supergroups.
    Returned only in getChat."""

    slow_mode_delay: Optional[int] = None
    """Optional. For supergroups, the minimum allowed delay between
    consecutive messages sent by each unpriviledged user; in seconds.
    Returned only in getChat."""

    message_auto_delete_time: Optional[int] = None
    """Optional. The time after which all messages sent to the chat will be
    automatically deleted; in seconds. Returned only in getChat."""

    has_protected_content: Optional[bool] = None
    """Optional. True, if messages from the chat can't be forwarded to other
    chats. Returned only in getChat."""

    sticker_set_name: Optional[str] = None
    """Optional. For supergroups, name of group sticker set. Returned only in
    getChat."""

    can_set_sticker_set: Optional[bool] = None
    """Optional. True, if the bot can change the group sticker set. Returned
    only in getChat."""

    linked_chat_id: Optional[int] = None
    """Optional. Unique identifier for the linked chat, i.e. the discussion
    group identifier for a channel and vice versa; for supergroups and
    channel chats. This identifier may be greater than 32 bits and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it is smaller than 52 bits, so a signed 64 bit
    integer or double-precision float type are safe for storing this
    identifier. Returned only in getChat."""

    location: Optional[ChatLocation] = None
    """Optional. For supergroups, the location to which the supergroup is
    connected. Returned only in getChat."""

    def adjust(self, bot: Bot):
        if self.pinned_message:
            self.pinned_message.adjust(bot)
