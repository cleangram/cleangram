from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .chat import Chat
from .base import TelegramType
from .chat_invite_link import ChatInviteLink
from .user import User


@dataclass
class ChatJoinRequest(TelegramType):
    """
    Represents a join request sent to a chat.
    Reference: https://core.telegram.org/bots/api#chatjoinrequest
    """

    chat: Chat
    """Chat to which the request was sent"""

    from_: User
    """User that sent the join request"""

    date: int
    """Date the request was sent in Unix time"""

    bio: Optional[str] = field(default=None)
    """Optional. Bio of the user."""

    invite_link: Optional[ChatInviteLink] = field(default=None)
    """Optional. Chat invite link that was used by the user to send
    the join request"""
