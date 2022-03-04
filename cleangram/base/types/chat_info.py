from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .base import TelegramType
from .chat_location import ChatLocation
from .chat_permissions import ChatPermissions
from .chat_photo import ChatPhoto
from .message import Message


@dataclass
class ChatInfo(TelegramType):
    """
    This object represents a chat.
    Reference: https://core.telegram.org/bots/api#chat
    """

    photo: Optional[ChatPhoto] = field(default=None)
    """Optional. Chat photo. Returned only in getChat."""

    bio: Optional[str] = field(default=None)
    """Optional. Bio of the other party in a private chat. Returned
    only in getChat."""

    has_private_forwards: Optional[bool] = field(default=None)
    """Optional. True, if privacy settings of the other party in
    the private chat allows to use tg://user?id=<user_id> links
    only in chats with the user. Returned only in getChat."""

    description: Optional[str] = field(default=None)
    """Optional. Description, for groups, supergroups and channel
    chats. Returned only in getChat."""

    invite_link: Optional[str] = field(default=None)
    """Optional. Primary invite link, for groups, supergroups and
    channel chats. Returned only in getChat."""

    pinned_message: Optional[Message] = field(default=None)
    """Optional. The most recent pinned message (by sending date).
    Returned only in getChat."""

    permissions: Optional[ChatPermissions] = field(default=None)
    """Optional. Default chat member permissions, for groups and
    supergroups. Returned only in getChat."""

    slow_mode_delay: Optional[int] = field(default=None)
    """Optional. For supergroups, the minimum allowed delay between
    consecutive messages sent by each unpriviledged user; in
    seconds. Returned only in getChat."""

    message_auto_delete_time: Optional[int] = field(default=None)
    """Optional. The time after which all messages sent to the chat
    will be automatically deleted; in seconds. Returned only in
    getChat."""

    has_protected_content: Optional[bool] = field(default=None)
    """Optional. True, if messages from the chat can't be forwarded
    to other chats. Returned only in getChat."""

    sticker_set_name: Optional[str] = field(default=None)
    """Optional. For supergroups, name of group sticker set.
    Returned only in getChat."""

    can_set_sticker_set: Optional[bool] = field(default=None)
    """Optional. True, if the bot can change the group sticker set.
    Returned only in getChat."""

    linked_chat_id: Optional[int] = field(default=None)
    """Optional. Unique identifier for the linked chat, i.e. the
    discussion group identifier for a channel and vice versa;
    for supergroups and channel chats. This identifier may be
    greater than 32 bits and some programming languages may have
    difficulty/silent defects in interpreting it. But it is
    smaller than 52 bits, so a signed 64 bit integer or double-
    precision float type are safe for storing this identifier.
    Returned only in getChat."""

    location: Optional[ChatLocation] = field(default=None)
    """Optional. For supergroups, the location to which the
    supergroup is connected. Returned only in getChat."""
