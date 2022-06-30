import abc
from typing import Optional, Union

from ...core.objects.response import Response
from ..bot.bot import Bot
from ..objects import Message, TelegramObject
from .base import TelegramPath


class SetGameScore(
    TelegramPath, abc.ABC, response=Response[Union[bool, Message]]
):
    """
    Use this method to set the score of the specified user in a game
    message. On success, if the message is not an inline message, the
    Message is returned, otherwise True is returned. Returns an error, if
    the new score is not greater than the user's current score in the chat
    and force is False.

    Reference: https://core.telegram.org/bots/api#setgamescore
    """

    user_id: int
    """User identifier"""

    score: int
    """New score, must be non-negative"""

    force: Optional[bool] = None
    """Pass True, if the high score is allowed to decrease. This can be
    useful when fixing mistakes or banning cheaters"""

    disable_edit_message: Optional[bool] = None
    """Pass True, if the game message should not be automatically edited to
    include the current scoreboard"""

    chat_id: Optional[int] = None
    """Required if inline_message_id is not specified. Unique identifier for
    the target chat"""

    message_id: Optional[int] = None
    """Required if inline_message_id is not specified. Identifier of the sent
    message"""

    inline_message_id: Optional[str] = None
    """Required if chat_id and message_id are not specified. Identifier of
    the inline message"""

    def adjust(self, bot: Bot, result: Union[bool, Message]):
        if isinstance(result, TelegramObject):
            result.adjust(bot)
