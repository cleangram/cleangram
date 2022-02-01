from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from cleangram.types import (
    Response,
    Message
)
from .base import TelegramMethod


@dataclass
class SetGameScore(TelegramMethod, response=Response[Union[Message, bool]]):
    """
    Use this method to set the score of the specified user in a
    game message. On success, if the message is not an inline
    message, the Message is returned, otherwise True is
    returned. Returns an error, if the new score is not greater
    than the user's current score in the chat and force is
    False.

    Reference: https://core.telegram.org/bots/api#setgamescore
    """

    user_id: int
    """User identifier"""

    score: int
    """New score, must be non-negative"""

    force: Optional[bool] = field(default=None)
    """Pass True, if the high score is allowed to decrease. This
    can be useful when fixing mistakes or banning cheaters"""

    disable_edit_message: Optional[bool] = field(default=None)
    """Pass True, if the game message should not be automatically
    edited to include the current scoreboard"""

    chat_id: Optional[int] = field(default=None)
    """Required if inline_message_id is not specified. Unique
    identifier for the target chat"""

    message_id: Optional[int] = field(default=None)
    """Required if inline_message_id is not specified. Identifier
    of the sent message"""

    inline_message_id: Optional[str] = field(default=None)
    """Required if chat_id and message_id are not specified.
    Identifier of the inline message"""
