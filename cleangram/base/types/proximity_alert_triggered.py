from __future__ import annotations

from dataclasses import dataclass


from .base import TelegramType
from .user import User


@dataclass
class ProximityAlertTriggered(TelegramType):
    """
    This object represents the content of a service message,
    sent whenever a user in the chat triggers a proximity alert
    set by another user.
    Reference: https://core.telegram.org/bots/api#proximityalerttriggered
    """

    traveler: User
    """User that triggered the alert"""

    watcher: User
    """User that set the alert"""

    distance: int
    """The distance between the users"""
