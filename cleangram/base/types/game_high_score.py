from __future__ import annotations

from dataclasses import dataclass

from .base import TelegramType
from .user import User


@dataclass
class GameHighScore(TelegramType):
    """
    This object represents one row of the high scores table for
    a game.
    Reference: https://core.telegram.org/bots/api#gamehighscore
    """

    position: int
    """Position in high score table for the game"""

    user: User
    """User"""

    score: int
    """Score"""
