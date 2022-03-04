from __future__ import annotations

from dataclasses import dataclass

from .base import TelegramType


@dataclass
class BotCommandScope(TelegramType):
    """
    This object represents the scope to which bot commands are
    applied. Currently, the following 7 scopes are supported:

        - BotCommandScopeDefault
        - BotCommandScopeAllPrivateChats
        - BotCommandScopeAllGroupChats
        - BotCommandScopeAllChatAdministrators
        - BotCommandScopeChat
        - BotCommandScopeChatAdministrators
        - BotCommandScopeChatMember

    Reference: https://core.telegram.org/bots/api#botcommandscope
    """
