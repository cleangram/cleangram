from __future__ import annotations

from dataclasses import dataclass

from .chat_member import ChatMember
from .user import User


@dataclass
class ChatMemberMember(ChatMember):
    """
    Represents a chat member that has no additional privileges
    or restrictions.
    Reference: https://core.telegram.org/bots/api#chatmembermember
    """

    status: str
    """The member's status in the chat, always “member”"""

    user: User
    """Information about the user"""
