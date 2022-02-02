from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from ..types import (
    InlineKeyboardMarkup,
    Message,
    Response
)
from .base import TelegramMethod


@dataclass
class StopMessageLiveLocation(TelegramMethod, response=Response[Union[Message, bool]]):
    """
    Use this method to stop updating a live location message
    before live_period expires. On success, if the message is
    not an inline message, the edited Message is returned,
    otherwise True is returned.

    Reference: https://core.telegram.org/bots/api#stopmessagelivelocation
    """

    chat_id: Optional[Union[str, int]] = field(default=None)
    """Required if inline_message_id is not specified. Unique
    identifier for the target chat or username of the target
    channel (in the format @channelusername)"""

    message_id: Optional[int] = field(default=None)
    """Required if inline_message_id is not specified. Identifier
    of the message with live location to stop"""

    inline_message_id: Optional[str] = field(default=None)
    """Required if chat_id and message_id are not specified.
    Identifier of the inline message"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """A JSON-serialized object for a new inline keyboard."""
