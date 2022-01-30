from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .location import Location
from .base import TelegramType
from .user import User


@dataclass
class ChosenInlineResult(TelegramType):
    """
    Represents a result of an inline query that was chosen by
    the user and sent to their chat partner.
    Reference: https://core.telegram.org/bots/api#choseninlineresult
    """

    result_id: str
    """The unique identifier for the result that was chosen"""

    from_: User
    """The user that chose the result"""

    query: str
    """The query that was used to obtain the result"""

    location: Optional[Location] = field(default=None)
    """Optional. Sender location, only for bots that require user
    location"""

    inline_message_id: Optional[str] = field(default=None)
    """Optional. Identifier of the sent inline message. Available
    only if there is an inline keyboard attached to the message.
    Will be also received in callback queries and can be used to
    edit the message."""
