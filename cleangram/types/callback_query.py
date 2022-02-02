from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .message import Message
from .base import TelegramType
from .user import User


@dataclass
class CallbackQuery(TelegramType):
    """
    This object represents an incoming callback query from a
    callback button in an inline keyboard. If the button that
    originated the query was attached to a message sent by the
    bot, the field message will be present. If the button was
    attached to a message sent via the bot (in inline mode), the
    field inline_message_id will be present. Exactly one of the
    fields data or game_short_name will be present.
    Reference: https://core.telegram.org/bots/api#callbackquery
    """

    id: str
    """Unique identifier for this query"""

    from_: User
    """Sender"""

    chat_instance: str
    """Global identifier, uniquely corresponding to the chat to
    which the message with the callback button was sent. Useful
    for high scores in games."""

    message: Optional[Message] = field(default=None)
    """Optional. Message with the callback button that originated
    the query. Note that message content and message date will
    not be available if the message is too old"""

    inline_message_id: Optional[str] = field(default=None)
    """Optional. Identifier of the message sent via the bot in
    inline mode, that originated the query."""

    data: Optional[str] = field(default=None)
    """Optional. Data associated with the callback button. Be aware
    that a bad client can send arbitrary data in this field."""

    game_short_name: Optional[str] = field(default=None)
    """Optional. Short name of a Game to be returned, serves as the
    unique identifier for the game"""
