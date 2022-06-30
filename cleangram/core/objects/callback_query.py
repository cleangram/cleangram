from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Optional

from pydantic import Field

from ..bot.bot import Bot
from .base import TelegramObject

if TYPE_CHECKING:
    from .message import Message
    from .user import User


class CallbackQuery(TelegramObject, abc.ABC):
    """
    This object represents an incoming callback query from a callback
    button in an inline keyboard. If the button that originated the query
    was attached to a message sent by the bot, the field message will be
    present. If the button was attached to a message sent via the bot (in
    inline mode), the field inline_message_id will be present. Exactly one
    of the fields data or game_short_name will be present.

    Reference: https://core.telegram.org/bots/api#callbackquery
    """

    id: str
    """Unique identifier for this query"""

    from_: User = Field(alias='from')
    """Sender"""

    chat_instance: str
    """Global identifier, uniquely corresponding to the chat to which the
    message with the callback button was sent. Useful for high scores in
    games."""

    message: Optional[Message] = None
    """Optional. Message with the callback button that originated the query.
    Note that message content and message date will not be available if
    the message is too old"""

    inline_message_id: Optional[str] = None
    """Optional. Identifier of the message sent via the bot in inline mode,
    that originated the query."""

    data: Optional[str] = None
    """Optional. Data associated with the callback button. Be aware that the
    message originated the query can contain no callback buttons with this
    data."""

    game_short_name: Optional[str] = None
    """Optional. Short name of a Game to be returned, serves as the unique
    identifier for the game"""

    def adjust(self, bot: Bot):
        if self.message:
            self.message.adjust(bot)
