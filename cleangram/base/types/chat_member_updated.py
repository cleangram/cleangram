from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .chat import Chat
from .chat_invite_link import ChatInviteLink
from .chat_member import ChatMember
from .base import TelegramType
from .user import User


@dataclass
class ChatMemberUpdated(TelegramType):
    """
    This object represents changes in the status of a chat
    member.
    Reference: https://core.telegram.org/bots/api#chatmemberupdated
    """

    chat: Chat
    """Chat the user belongs to"""

    from_: User
    """Performer of the action, which resulted in the change"""

    date: int
    """Date the change was done in Unix time"""

    old_chat_member: ChatMember
    """Previous information about the chat member"""

    new_chat_member: ChatMember
    """New information about the chat member"""

    invite_link: Optional[ChatInviteLink] = field(default=None)
    """Optional. Chat invite link, which was used by the user to
    join the chat; for joining by invite link events only."""
