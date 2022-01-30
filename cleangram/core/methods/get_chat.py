from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from ..types import (
    Response,
    ChatInfo
)
from .base import TelegramMethod


@dataclass
class GetChat(TelegramMethod, response=Response[ChatInfo]):
    """
    Use this method to get up to date information about the chat
    (current name of the user for one-on-one conversations,
    current username of a user, group or channel, etc.). Returns
    a Chat object on success.

    Reference: https://core.telegram.org/bots/api#getchat
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target supergroup or channel (in the format
    @channelusername)"""
