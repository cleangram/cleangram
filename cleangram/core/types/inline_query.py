from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .location import Location
from .base import TelegramType
from .user import User


@dataclass
class InlineQuery(TelegramType):
    """
    This object represents an incoming inline query. When the
    user sends an empty query, your bot could return some
    default or trending results.
    Reference: https://core.telegram.org/bots/api#inlinequery
    """

    id: str
    """Unique identifier for this query"""

    from_: User
    """Sender"""

    query: str
    """Text of the query (up to 256 characters)"""

    offset: str
    """Offset of the results to be returned, can be controlled by
    the bot"""

    chat_type: Optional[str] = field(default=None)
    """Optional. Type of the chat, from which the inline query was
    sent. Can be either “sender” for a private chat with the
    inline query sender, “private”, “group”, “supergroup”, or
    “channel”. The chat type should be always known for requests
    sent from official clients and most third-party clients,
    unless the request was sent from a secret chat"""

    location: Optional[Location] = field(default=None)
    """Optional. Sender location, only for bots that request user
    location"""
