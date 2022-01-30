from __future__ import annotations

from dataclasses import dataclass


from .chat_member import ChatMember
from .user import User


@dataclass
class ChatMemberLeft(ChatMember):
    """
    Represents a chat member that isn't currently a member of
    the chat, but may join it themselves.
    Reference: https://core.telegram.org/bots/api#chatmemberleft
    """

    status: str
    """The member's status in the chat, always “left”"""

    user: User
    """Information about the user"""
