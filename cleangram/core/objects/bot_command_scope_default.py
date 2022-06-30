from __future__ import annotations

from .bot_command_scope import BotCommandScope


class BotCommandScopeDefault(BotCommandScope):
    """
    Represents the default scope of bot commands. Default commands are
    used if no commands with a narrower scope are specified for the user.

    Reference: https://core.telegram.org/bots/api#botcommandscopedefault
    """

    type: str = 'default'
    """Scope type, must be default"""
