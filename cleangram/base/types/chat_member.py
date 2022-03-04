from __future__ import annotations

from dataclasses import dataclass

from .base import TelegramType


@dataclass
class ChatMember(TelegramType):
    """
    This object contains information about one member of a chat.
    Currently, the following 6 types of chat members are
    supported:

        - ChatMemberOwner
        - ChatMemberAdministrator
        - ChatMemberMember
        - ChatMemberRestricted
        - ChatMemberLeft
        - ChatMemberBanned

    Reference: https://core.telegram.org/bots/api#chatmember
    """
