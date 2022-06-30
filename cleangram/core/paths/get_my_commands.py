from typing import List, Optional

from ...core.objects.response import Response
from ..objects import BotCommand, BotCommandScope
from .base import TelegramPath


class GetMyCommands(TelegramPath, response=Response[List[BotCommand]]):
    """
    Use this method to get the current list of the bot's commands for the
    given scope and user language. Returns Array of BotCommand on success.
    If commands aren't set, an empty list is returned.

    Reference: https://core.telegram.org/bots/api#getmycommands
    """

    scope: Optional[BotCommandScope] = None
    """A JSON-serialized object, describing scope of users. Defaults to
    BotCommandScopeDefault."""

    language_code: Optional[str] = None
    """A two-letter ISO 639-1 language code or an empty string"""
