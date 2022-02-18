from __future__ import annotations

from dataclasses import dataclass, field


from .bot_command_scope import BotCommandScope


@dataclass
class BotCommandScopeDefault(BotCommandScope):
    """
    Represents the default scope of bot commands. Default
    commands are used if no commands with a narrower scope are
    specified for the user.
    Reference: https://core.telegram.org/bots/api#botcommandscopedefault
    """

    type_: str = field(default="")
    """Scope type, must be default"""

    def __post_init__(self):
        self.type_ = "default"
