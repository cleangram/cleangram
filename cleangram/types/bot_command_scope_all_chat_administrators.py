from __future__ import annotations

from dataclasses import dataclass, InitVar, field


from .bot_command_scope import BotCommandScope


@dataclass
class BotCommandScopeAllChatAdministrators(BotCommandScope):
    """
    Represents the scope of bot commands, covering all group and
    supergroup chat administrators.
    Reference: https://core.telegram.org/bots/api#botcommandscopeallchatadministrators
    """

    type_: str = field(default='all_chat_administrators')
    """Scope type, must be all_chat_administrators"""
