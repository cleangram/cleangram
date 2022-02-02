from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from ..types import (
    BotCommand,
    BotCommandScope,
    Response
)
from .base import TelegramMethod


@dataclass
class SetMyCommands(TelegramMethod, response=Response[bool]):
    """
    Use this method to change the list of the bot's commands.
    See https://core.telegram.org/bots#commands for more details
    about bot commands. Returns True on success.

    Reference: https://core.telegram.org/bots/api#setmycommands
    """

    commands: List[BotCommand]
    """A JSON-serialized list of bot commands to be set as the list
    of the bot's commands. At most 100 commands can be
    specified."""

    scope: Optional[BotCommandScope] = field(default=None)
    """A JSON-serialized object, describing scope of users for
    which the commands are relevant. Defaults to
    BotCommandScopeDefault."""

    language_code: Optional[str] = field(default=None)
    """A two-letter ISO 639-1 language code. If empty, commands
    will be applied to all users from the given scope, for whose
    language there are no dedicated commands"""
