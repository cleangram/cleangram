from __future__ import annotations

from dataclasses import dataclass, InitVar, field
from typing import Optional

from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query_result import InlineQueryResult


@dataclass
class InlineQueryResultGame(InlineQueryResult):
    """
    Represents a Game.
    Reference: https://core.telegram.org/bots/api#inlinequeryresultgame
    """

    id: str
    """Unique identifier for this result, 1-64 bytes"""

    game_short_name: str
    """Short name of the game"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""

    type_: str = field(default='game')
    """Type of the result, must be game"""
