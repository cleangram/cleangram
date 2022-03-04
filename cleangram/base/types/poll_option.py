from __future__ import annotations

from dataclasses import dataclass

from .base import TelegramType


@dataclass
class PollOption(TelegramType):
    """
    This object contains information about one answer option in
    a poll.
    Reference: https://core.telegram.org/bots/api#polloption
    """

    text: str
    """Option text, 1-100 characters"""

    voter_count: int
    """Number of users that voted for this option"""
