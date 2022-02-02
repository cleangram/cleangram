from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from ..types import (
    Response
)
from .base import TelegramMethod


@dataclass
class DeclineChatJoinRequest(TelegramMethod, response=Response[bool]):
    """
    Use this method to decline a chat join request. The bot must
    be an administrator in the chat for this to work and must
    have the can_invite_users administrator right. Returns True
    on success.

    Reference: https://core.telegram.org/bots/api#declinechatjoinrequest
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    user_id: int
    """Unique identifier of the target user"""
