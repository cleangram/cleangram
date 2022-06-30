from __future__ import annotations

from .base import TelegramObject


class ChatMember(TelegramObject):
    """
    This object contains information about one member of a chat.
    Currently, the following 6 types of chat members are supported:

        :class:`cleangram.ChatMemberOwner`
        :class:`cleangram.ChatMemberAdministrator`
        :class:`cleangram.ChatMemberMember`
        :class:`cleangram.ChatMemberRestricted`
        :class:`cleangram.ChatMemberLeft`
        :class:`cleangram.ChatMemberBanned`

    Reference: https://core.telegram.org/bots/api#chatmember
    """
