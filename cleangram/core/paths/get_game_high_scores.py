from typing import List, Optional

from ...core.objects.response import Response
from ..objects import GameHighScore
from .base import TelegramPath


class GetGameHighScores(TelegramPath, response=Response[List[GameHighScore]]):
    """
    Use this method to get data for high score tables. Will return the
    score of the specified user and several of their neighbors in a game.
    On success, returns an Array of GameHighScore objects.

    Reference: https://core.telegram.org/bots/api#getgamehighscores
    """

    user_id: int
    """Target user id"""

    chat_id: Optional[int] = None
    """Required if inline_message_id is not specified. Unique identifier for
    the target chat"""

    message_id: Optional[int] = None
    """Required if inline_message_id is not specified. Identifier of the sent
    message"""

    inline_message_id: Optional[str] = None
    """Required if chat_id and message_id are not specified. Identifier of
    the inline message"""
