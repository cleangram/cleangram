from __future__ import annotations

from dataclasses import dataclass

from .chat_member import ChatMember
from .user import User


@dataclass
class ChatMemberBanned(ChatMember):
    """
    Represents a chat member that was banned in the chat and
    can't return to the chat or view chat messages.
    Reference: https://core.telegram.org/bots/api#chatmemberbanned
    """

    status: str
    """The member's status in the chat, always “kicked”"""

    user: User
    """Information about the user"""

    until_date: int
    """Date when restrictions will be lifted for this user; unix
    time. If 0, then the user is banned forever"""
