from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from cleangram.types import (
    Response
)
from .base import TelegramMethod


@dataclass
class GetChatMemberCount(TelegramMethod, response=Response[int]):
    """
    Use this method to get the number of members in a chat.
    Returns Int on success.

    Reference: https://core.telegram.org/bots/api#getchatmembercount
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target supergroup or channel (in the format
    @channelusername)"""
