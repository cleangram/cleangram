from typing import Optional

from ...core.objects.response import Response
from ..objects import BotCommandScope
from .base import TelegramPath


class DeleteMyCommands(TelegramPath, response=Response[bool]):
    """
    Use this method to delete the list of the bot's commands for the given
    scope and user language. After deletion, higher level commands will be
    shown to affected users. Returns True on success.

    Reference: https://core.telegram.org/bots/api#deletemycommands
    """

    scope: Optional[BotCommandScope] = None
    """A JSON-serialized object, describing scope of users for which the
    commands are relevant. Defaults to BotCommandScopeDefault."""

    language_code: Optional[str] = None
    """A two-letter ISO 639-1 language code. If empty, commands will be
    applied to all users from the given scope, for whose language there
    are no dedicated commands"""
