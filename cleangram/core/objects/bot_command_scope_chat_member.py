from __future__ import annotations

from typing import Union

from .bot_command_scope import BotCommandScope


class BotCommandScopeChatMember(BotCommandScope):
    """
    Represents the scope of bot commands, covering a specific member of a
    group or supergroup chat.

    Reference: https://core.telegram.org/bots/api#botcommandscopechatmember
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    supergroup (in the format @supergroupusername)"""

    user_id: int
    """Unique identifier of the target user"""

    type: str = 'chat_member'
    """Scope type, must be chat_member"""
