from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from cleangram.types import (
    InlineKeyboardMarkup,
    Response,
    Poll
)
from .base import TelegramMethod


@dataclass
class StopPoll(TelegramMethod, response=Response[Poll]):
    """
    Use this method to stop a poll which was sent by the bot. On
    success, the stopped Poll is returned.

    Reference: https://core.telegram.org/bots/api#stoppoll
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    message_id: int
    """Identifier of the original message with the poll"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """A JSON-serialized object for a new message inline keyboard."""
