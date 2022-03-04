from __future__ import annotations

from dataclasses import dataclass

from .base import TelegramType
from .location import Location


@dataclass
class ChatLocation(TelegramType):
    """
    Represents a location to which a chat is connected.
    Reference: https://core.telegram.org/bots/api#chatlocation
    """

    location: Location
    """The location to which the supergroup is connected. Can't be
    a live location."""

    address: str
    """Location address; 1-64 characters, as defined by the chat
    owner"""
