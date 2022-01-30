from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .base import TelegramType


@dataclass
class Chat(TelegramType):
    """
    This object represents a chat.
    Reference: https://core.telegram.org/bots/api#chat
    """

    id: int
    """Unique identifier for this chat. This number may have more
    than 32 significant bits and some programming languages may
    have difficulty/silent defects in interpreting it. But it
    has at most 52 significant bits, so a signed 64-bit integer
    or double-precision float type are safe for storing this
    identifier."""

    type_: str
    """Type of chat, can be either “private”, “group”, “supergroup”
    or “channel”"""

    title: Optional[str] = field(default=None)
    """Optional. Title, for supergroups, channels and group chats"""

    username: Optional[str] = field(default=None)
    """Optional. Username, for private chats, supergroups and
    channels if available"""

    first_name: Optional[str] = field(default=None)
    """Optional. First name of the other party in a private chat"""

    last_name: Optional[str] = field(default=None)
    """Optional. Last name of the other party in a private chat"""
