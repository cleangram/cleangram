from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from cleangram.types import (
    Response
)
from .base import TelegramMethod


@dataclass
class SetChatAdministratorCustomTitle(TelegramMethod, response=Response[bool]):
    """
    Use this method to set a custom title for an administrator
    in a supergroup promoted by the bot. Returns True on
    success.

    Reference: https://core.telegram.org/bots/api#setchatadministratorcustomtitle
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target supergroup (in the format @supergroupusername)"""

    user_id: int
    """Unique identifier of the target user"""

    custom_title: str
    """New custom title for the administrator; 0-16 characters,
    emoji are not allowed"""
