from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, List

from ..types import (
    Response,
    GameHighScore
)
from .base import TelegramMethod


@dataclass
class GetGameHighScores(TelegramMethod, response=Response[List[GameHighScore]]):
    """
    Use this method to get data for high score tables. Will
    return the score of the specified user and several of their
    neighbors in a game. On success, returns an Array of
    GameHighScore objects.

    Reference: https://core.telegram.org/bots/api#getgamehighscores
    """

    user_id: int
    """Target user id"""

    chat_id: Optional[int] = field(default=None)
    """Required if inline_message_id is not specified. Unique
    identifier for the target chat"""

    message_id: Optional[int] = field(default=None)
    """Required if inline_message_id is not specified. Identifier
    of the sent message"""

    inline_message_id: Optional[str] = field(default=None)
    """Required if chat_id and message_id are not specified.
    Identifier of the inline message"""
