from __future__ import annotations

from .base import TelegramObject


class BotCommandScope(TelegramObject):
    """
    This object represents the scope to which bot commands are applied.
    Currently, the following 7 scopes are supported:

        :class:`cleangram.BotCommandScopeDefault`
        :class:`cleangram.BotCommandScopeAllPrivateChats`
        :class:`cleangram.BotCommandScopeAllGroupChats`
        :class:`cleangram.BotCommandScopeAllChatAdministrators`
        :class:`cleangram.BotCommandScopeChat`
        :class:`cleangram.BotCommandScopeChatAdministrators`
        :class:`cleangram.BotCommandScopeChatMember`

    Reference: https://core.telegram.org/bots/api#botcommandscope
    """
