from __future__ import annotations

from typing import Union

from .bot_command_scope import BotCommandScope


class BotCommandScopeChat(BotCommandScope):
    """
    Represents the scope of bot commands, covering a specific chat.

    Reference: https://core.telegram.org/bots/api#botcommandscopechat
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    supergroup (in the format @supergroupusername)"""

    type: str = 'chat'
    """Scope type, must be chat"""
