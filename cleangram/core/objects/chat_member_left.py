from __future__ import annotations

from typing import TYPE_CHECKING

from .chat_member import ChatMember

if TYPE_CHECKING:
    from .user import User


class ChatMemberLeft(ChatMember):
    """
    Represents a chat member that isn't currently a member of the chat,
    but may join it themselves.

    Reference: https://core.telegram.org/bots/api#chatmemberleft
    """

    status: str
    """The member's status in the chat, always “left”"""

    user: User
    """Information about the user"""
