from __future__ import annotations

from dataclasses import dataclass, field, InitVar


from .bot_command_scope import BotCommandScope


@dataclass
class BotCommandScopeAllGroupChats(BotCommandScope):
    """
    Represents the scope of bot commands, covering all group and
    supergroup chats.
    Reference: https://core.telegram.org/bots/api#botcommandscopeallgroupchats
    """

    type_: str = field(default='all_group_chats')
    """Scope type, must be all_group_chats"""
