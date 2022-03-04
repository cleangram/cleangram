from __future__ import annotations

from dataclasses import dataclass

from .base import TelegramType


@dataclass
class MessageAutoDeleteTimerChanged(TelegramType):
    """
    This object represents a service message about a change in
    auto-delete timer settings.
    Reference: https://core.telegram.org/bots/api#messageautodeletetimerchanged
    """

    message_auto_delete_time: int
    """New auto-delete time for messages in the chat; in seconds"""
