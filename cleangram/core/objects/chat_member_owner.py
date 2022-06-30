from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from .chat_member import ChatMember

if TYPE_CHECKING:
    from .user import User


class ChatMemberOwner(ChatMember):
    """
    Represents a chat member that owns the chat and has all administrator
    privileges.

    Reference: https://core.telegram.org/bots/api#chatmemberowner
    """

    status: str
    """The member's status in the chat, always “creator”"""

    user: User
    """Information about the user"""

    is_anonymous: bool
    """True, if the user's presence in the chat is hidden"""

    custom_title: Optional[str] = None
    """Optional. Custom title for this user"""
