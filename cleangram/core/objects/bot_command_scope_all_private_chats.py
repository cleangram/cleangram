from __future__ import annotations

from .bot_command_scope import BotCommandScope


class BotCommandScopeAllPrivateChats(BotCommandScope):
    """
    Represents the scope of bot commands, covering all private chats.

    Reference: https://core.telegram.org/bots/api#botcommandscopeallprivatechats
    """

    type: str = 'all_private_chats'
    """Scope type, must be all_private_chats"""
