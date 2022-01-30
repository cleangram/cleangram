from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .base import TelegramType


@dataclass
class KeyboardButtonPollType(TelegramType):
    """
    This object represents type of a poll, which is allowed to
    be created and sent when the corresponding button is
    pressed.
    Reference: https://core.telegram.org/bots/api#keyboardbuttonpolltype
    """

    type_: Optional[str] = field(default=None)
    """Optional. If quiz is passed, the user will be allowed to
    create only polls in the quiz mode. If regular is passed,
    only regular polls will be allowed. Otherwise, the user will
    be allowed to create a poll of any type."""
