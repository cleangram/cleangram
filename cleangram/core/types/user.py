from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .base import TelegramType


@dataclass
class User(TelegramType):
    """
    This object represents a Telegram user or bot.
    Reference: https://core.telegram.org/bots/api#user
    """

    id: int
    """Unique identifier for this user or bot. This number may have
    more than 32 significant bits and some programming languages
    may have difficulty/silent defects in interpreting it. But
    it has at most 52 significant bits, so a 64-bit integer or
    double-precision float type are safe for storing this
    identifier."""

    is_bot: bool
    """True, if this user is a bot"""

    first_name: str
    """User's or bot's first name"""

    last_name: Optional[str] = field(default=None)
    """Optional. User's or bot's last name"""

    username: Optional[str] = field(default=None)
    """Optional. User's or bot's username"""

    language_code: Optional[str] = field(default=None)
    """Optional. IETF language tag of the user's language"""

    can_join_groups: Optional[bool] = field(default=None)
    """Optional. True, if the bot can be invited to groups.
    Returned only in getMe."""

    can_read_all_group_messages: Optional[bool] = field(default=None)
    """Optional. True, if privacy mode is disabled for the bot.
    Returned only in getMe."""

    supports_inline_queries: Optional[bool] = field(default=None)
    """Optional. True, if the bot supports inline queries. Returned
    only in getMe."""
