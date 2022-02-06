from __future__ import annotations

from dataclasses import dataclass, field, InitVar
from typing import Union

from .bot_command_scope import BotCommandScope


@dataclass
class BotCommandScopeChatMember(BotCommandScope):
    """
    Represents the scope of bot commands, covering a specific
    member of a group or supergroup chat.
    Reference: https://core.telegram.org/bots/api#botcommandscopechatmember
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target supergroup (in the format @supergroupusername)"""

    user_id: int
    """Unique identifier of the target user"""

    type_: str = field(default="chat_member")
    """Scope type, must be chat_member"""
