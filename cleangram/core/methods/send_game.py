from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ..types import (
    InlineKeyboardMarkup,
    Response,
    Message
)
from .base import TelegramMethod


@dataclass
class SendGame(TelegramMethod, response=Response[Message]):
    """
    Use this method to send a game. On success, the sent Message
    is returned.

    Reference: https://core.telegram.org/bots/api#sendgame
    """

    chat_id: int
    """Unique identifier for the target chat"""

    game_short_name: str
    """Short name of the game, serves as the unique identifier for
    the game. Set up your games via Botfather."""

    disable_notification: Optional[bool] = field(default=None)
    """Sends the message silently. Users will receive a
    notification with no sound."""

    protect_content: Optional[bool] = field(default=None)
    """Protects the contents of the sent message from forwarding
    and saving"""

    reply_to_message_id: Optional[int] = field(default=None)
    """If the message is a reply, ID of the original message"""

    allow_sending_without_reply: Optional[bool] = field(default=None)
    """Pass True, if the message should be sent even if the
    specified replied-to message is not found"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """A JSON-serialized object for an inline keyboard. If empty,
    one 'Play game_title' button will be shown. If not empty,
    the first button must launch the game."""
