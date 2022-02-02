from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from .message_entity import MessageEntity
from .poll_option import PollOption
from .base import TelegramType


@dataclass
class Poll(TelegramType):
    """
    This object contains information about a poll.
    Reference: https://core.telegram.org/bots/api#poll
    """

    id: str
    """Unique poll identifier"""

    question: str
    """Poll question, 1-300 characters"""

    options: List[PollOption]
    """List of poll options"""

    total_voter_count: int
    """Total number of users that voted in the poll"""

    is_closed: bool
    """True, if the poll is closed"""

    is_anonymous: bool
    """True, if the poll is anonymous"""

    type_: str
    """Poll type, currently can be “regular” or “quiz”"""

    allows_multiple_answers: bool
    """True, if the poll allows multiple answers"""

    correct_option_id: Optional[int] = field(default=None)
    """Optional. 0-based identifier of the correct answer option.
    Available only for polls in the quiz mode, which are closed,
    or was sent (not forwarded) by the bot or to the private
    chat with the bot."""

    explanation: Optional[str] = field(default=None)
    """Optional. Text that is shown when a user chooses an
    incorrect answer or taps on the lamp icon in a quiz-style
    poll, 0-200 characters"""

    explanation_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. Special entities like usernames, URLs, bot
    commands, etc. that appear in the explanation"""

    open_period: Optional[int] = field(default=None)
    """Optional. Amount of time in seconds the poll will be active
    after creation"""

    close_date: Optional[int] = field(default=None)
    """Optional. Point in time (Unix timestamp) when the poll will
    be automatically closed"""
