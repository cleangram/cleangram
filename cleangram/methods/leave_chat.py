from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from ..types import (
    Response
)
from .base import TelegramMethod


@dataclass
class LeaveChat(TelegramMethod, response=Response[bool]):
    """
    Use this method for your bot to leave a group, supergroup or
    channel. Returns True on success.

    Reference: https://core.telegram.org/bots/api#leavechat
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target supergroup or channel (in the format
    @channelusername)"""
