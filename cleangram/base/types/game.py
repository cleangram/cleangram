from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from .animation import Animation
from .message_entity import MessageEntity
from .photo_size import PhotoSize
from .base import TelegramType


@dataclass
class Game(TelegramType):
    """
    This object represents a game. Use BotFather to create and
    edit games, their short names will act as unique
    identifiers.
    Reference: https://core.telegram.org/bots/api#game
    """

    title: str
    """Title of the game"""

    description: str
    """Description of the game"""

    photo: List[PhotoSize]
    """Photo that will be displayed in the game message in chats."""

    text: Optional[str] = field(default=None)
    """Optional. Brief description of the game or high scores
    included in the game message. Can be automatically edited to
    include current high scores for the game when the bot calls
    setGameScore, or manually edited using editMessageText.
    0-4096 characters."""

    text_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. Special entities that appear in text, such as
    usernames, URLs, bot commands, etc."""

    animation: Optional[Animation] = field(default=None)
    """Optional. Animation that will be displayed in the game
    message in chats. Upload via BotFather"""
