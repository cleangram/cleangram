from typing import List, Optional

from ...core.objects.response import Response
from ..objects import BotCommand, BotCommandScope
from .base import TelegramPath


class SetMyCommands(TelegramPath, response=Response[bool]):
    """
    Use this method to change the list of the bot's commands. See
    https://core.telegram.org/bots#commands for more details about bot
    commands. Returns True on success.

    Reference: https://core.telegram.org/bots/api#setmycommands
    """

    commands: List[BotCommand]
    """A JSON-serialized list of bot commands to be set as the list of the
    bot's commands. At most 100 commands can be specified."""

    scope: Optional[BotCommandScope] = None
    """A JSON-serialized object, describing scope of users for which the
    commands are relevant. Defaults to BotCommandScopeDefault."""

    language_code: Optional[str] = None
    """A two-letter ISO 639-1 language code. If empty, commands will be
    applied to all users from the given scope, for whose language there
    are no dedicated commands"""
