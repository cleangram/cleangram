from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from ..types import (
    ChatMember,
    Response
)
from .base import TelegramMethod


@dataclass
class GetChatMember(TelegramMethod, response=Response[ChatMember]):
    """
    Use this method to get information about a member of a chat.
    Returns a ChatMember object on success.

    Reference: https://core.telegram.org/bots/api#getchatmember
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target supergroup or channel (in the format
    @channelusername)"""

    user_id: int
    """Unique identifier of the target user"""
