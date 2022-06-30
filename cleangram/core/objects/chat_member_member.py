from __future__ import annotations

from typing import TYPE_CHECKING

from .chat_member import ChatMember

if TYPE_CHECKING:
    from .user import User


class ChatMemberMember(ChatMember):
    """
    Represents a chat member that has no additional privileges or
    restrictions.

    Reference: https://core.telegram.org/bots/api#chatmembermember
    """

    status: str
    """The member's status in the chat, always “member”"""

    user: User
    """Information about the user"""
