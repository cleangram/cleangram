from __future__ import annotations

from dataclasses import dataclass


from .base import TelegramType


@dataclass
class BotCommand(TelegramType):
    """
    This object represents a bot command.
    Reference: https://core.telegram.org/bots/api#botcommand
    """

    command: str
    """Text of the command; 1-32 characters. Can contain only
    lowercase English letters, digits and underscores."""

    description: str
    """Description of the command; 1-256 characters."""
