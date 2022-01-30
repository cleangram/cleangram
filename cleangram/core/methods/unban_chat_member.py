from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from ..types import (
    Response
)
from .base import TelegramMethod


@dataclass
class UnbanChatMember(TelegramMethod, response=Response[bool]):
    """
    Use this method to unban a previously banned user in a
    supergroup or channel. The user will not return to the group
    or channel automatically, but will be able to join via link,
    etc. The bot must be an administrator for this to work. By
    default, this method guarantees that after the call the user
    is not a member of the chat, but will be able to join it. So
    if the user is a member of the chat they will also be
    removed from the chat. If you don't want this, use the
    parameter only_if_banned. Returns True on success.

    Reference: https://core.telegram.org/bots/api#unbanchatmember
    """

    chat_id: Union[str, int]
    """Unique identifier for the target group or username of the
    target supergroup or channel (in the format @username)"""

    user_id: int
    """Unique identifier of the target user"""

    only_if_banned: Optional[bool] = field(default=None)
    """Do nothing if the user is not banned"""
