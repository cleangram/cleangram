from __future__ import annotations

from dataclasses import dataclass, field, InitVar


from .bot_command_scope import BotCommandScope


@dataclass
class BotCommandScopeAllPrivateChats(BotCommandScope):
    """
    Represents the scope of bot commands, covering all private
    chats.
    Reference: https://core.telegram.org/bots/api#botcommandscopeallprivatechats
    """

    type_: str = field(default="all_private_chats")
    """Scope type, must be all_private_chats"""
