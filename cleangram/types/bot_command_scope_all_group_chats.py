from __future__ import annotations

from dataclasses import dataclass, field


from .bot_command_scope import BotCommandScope


@dataclass
class BotCommandScopeAllGroupChats(BotCommandScope):
    """
    Represents the scope of bot commands, covering all group and
    supergroup chats.
    Reference: https://core.telegram.org/bots/api#botcommandscopeallgroupchats
    """

    type_: str = field(default="")
    """Scope type, must be all_group_chats"""

    def __post_init__(self):
        self.type_ = "all_group_chats"
