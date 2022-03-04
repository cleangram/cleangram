from __future__ import annotations

from dataclasses import dataclass

from .base import TelegramType


@dataclass
class MessageId(TelegramType):
    """
    This object represents a unique message identifier.
    Reference: https://core.telegram.org/bots/api#messageid
    """

    message_id: int
    """Unique message identifier"""
