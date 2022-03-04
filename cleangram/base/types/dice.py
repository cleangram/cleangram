from __future__ import annotations

from dataclasses import dataclass

from .base import TelegramType


@dataclass
class Dice(TelegramType):
    """
    This object represents an animated emoji that displays a
    random value.
    Reference: https://core.telegram.org/bots/api#dice
    """

    emoji: str
    """Emoji on which the dice throw animation is based"""

    value: int
    """Value of the dice, 1-6 for “”, “” and “” base emoji, 1-5 for
    “” and “” base emoji, 1-64 for “” base emoji"""
