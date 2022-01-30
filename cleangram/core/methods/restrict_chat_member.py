from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from ..types import (
    Response,
    ChatPermissions
)
from .base import TelegramMethod


@dataclass
class RestrictChatMember(TelegramMethod, response=Response[bool]):
    """
    Use this method to restrict a user in a supergroup. The bot
    must be an administrator in the supergroup for this to work
    and must have the appropriate administrator rights. Pass
    True for all permissions to lift restrictions from a user.
    Returns True on success.

    Reference: https://core.telegram.org/bots/api#restrictchatmember
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target supergroup (in the format @supergroupusername)"""

    user_id: int
    """Unique identifier of the target user"""

    permissions: ChatPermissions
    """A JSON-serialized object for new user permissions"""

    until_date: Optional[int] = field(default=None)
    """Date when restrictions will be lifted for the user, unix
    time. If user is restricted for more than 366 days or less
    than 30 seconds from the current time, they are considered
    to be restricted forever"""
