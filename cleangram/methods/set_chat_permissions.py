from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from cleangram.types import (
    Response,
    ChatPermissions
)
from .base import TelegramMethod


@dataclass
class SetChatPermissions(TelegramMethod, response=Response[bool]):
    """
    Use this method to set default chat permissions for all
    members. The bot must be an administrator in the group or a
    supergroup for this to work and must have the
    can_restrict_members administrator rights. Returns True on
    success.

    Reference: https://core.telegram.org/bots/api#setchatpermissions
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target supergroup (in the format @supergroupusername)"""

    permissions: ChatPermissions
    """A JSON-serialized object for new default chat permissions"""
