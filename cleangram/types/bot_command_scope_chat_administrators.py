from __future__ import annotations

from dataclasses import dataclass, InitVar, field
from typing import Union

from .bot_command_scope import BotCommandScope


@dataclass
class BotCommandScopeChatAdministrators(BotCommandScope):
    """
    Represents the scope of bot commands, covering all
    administrators of a specific group or supergroup chat.
    Reference: https://core.telegram.org/bots/api#botcommandscopechatadministrators
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target supergroup (in the format @supergroupusername)"""

    type_: str = field(default='chat_administrators')
    """Scope type, must be chat_administrators"""
