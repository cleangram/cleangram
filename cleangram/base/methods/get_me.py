from __future__ import annotations

from dataclasses import dataclass

from ..types import Response, User
from .base import TelegramMethod


@dataclass
class GetMe(TelegramMethod, response=Response[User]):
    """
    A simple method for testing your bot's authentication token.
    Requires no parameters. Returns basic information about the
    bot in form of a User object.

    Reference: https://core.telegram.org/bots/api#getme
    """
