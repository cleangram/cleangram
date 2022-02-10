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

    type_: str = field(default='')
    """Scope type, must be all_private_chats"""

    def __post_init__(self):
        self.type_ = "all_private_chats"
    