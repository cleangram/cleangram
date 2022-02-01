from __future__ import annotations

from dataclasses import dataclass


from .base import TelegramType


@dataclass
class CallbackGame(TelegramType):
    """
    A placeholder, currently holds no information. Use BotFather
    to set up your game.
    Reference: https://core.telegram.org/bots/api#callbackgame
    """
