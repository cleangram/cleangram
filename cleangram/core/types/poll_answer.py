from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .base import TelegramType
from .user import User


@dataclass
class PollAnswer(TelegramType):
    """
    This object represents an answer of a user in a non-
    anonymous poll.
    Reference: https://core.telegram.org/bots/api#pollanswer
    """

    poll_id: str
    """Unique poll identifier"""

    user: User
    """The user, who changed the answer to the poll"""

    option_ids: List[int]
    """0-based identifiers of answer options, chosen by the user.
    May be empty if the user retracted their vote."""
