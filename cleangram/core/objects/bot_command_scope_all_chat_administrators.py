from __future__ import annotations

from .bot_command_scope import BotCommandScope


class BotCommandScopeAllChatAdministrators(BotCommandScope):
    """
    Represents the scope of bot commands, covering all group and
    supergroup chat administrators.

    Reference: https://core.telegram.org/bots/api#botcommandscopeallchatadministrators
    """

    type: str = 'all_chat_administrators'
    """Scope type, must be all_chat_administrators"""
