from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from .inline_query_result import InlineQueryResult

if TYPE_CHECKING:
    from .inline_keyboard_markup import InlineKeyboardMarkup


class InlineQueryResultGame(InlineQueryResult):
    """
    Represents a Game.
    Note: This will only work in Telegram versions released after October
    1, 2016. Older clients will not display any inline results if a game
    result is among them.

    Reference: https://core.telegram.org/bots/api#inlinequeryresultgame
    """

    id: str
    """Unique identifier for this result, 1-64 bytes"""

    game_short_name: str
    """Short name of the game"""

    reply_markup: Optional[InlineKeyboardMarkup] = None
    """Optional. Inline keyboard attached to the message"""

    type: str = 'game'
    """Type of the result, must be game"""
