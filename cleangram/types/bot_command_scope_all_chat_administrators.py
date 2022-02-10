from __future__ import annotations

from dataclasses import dataclass, field


from .bot_command_scope import BotCommandScope


@dataclass
class BotCommandScopeAllChatAdministrators(BotCommandScope):
    """
    Represents the scope of bot commands, covering all group and
    supergroup chat administrators.
    Reference: https://core.telegram.org/bots/api#botcommandscopeallchatadministrators
    """

    type_: str = field(default="")
    """Scope type, must be all_chat_administrators"""

    def __post_init__(self):
        self.type_ = "all_chat_administrators"
