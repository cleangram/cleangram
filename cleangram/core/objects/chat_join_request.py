from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Optional

from pydantic import Field

from ..bot.bot import Bot
from .base import TelegramObject

if TYPE_CHECKING:
    from .chat import Chat
    from .chat_invite_link import ChatInviteLink
    from .user import User


class ChatJoinRequest(TelegramObject, abc.ABC):
    """
    Represents a join request sent to a chat.

    Reference: https://core.telegram.org/bots/api#chatjoinrequest
    """

    chat: Chat
    """Chat to which the request was sent"""

    from_: User = Field(alias='from')
    """User that sent the join request"""

    date: int
    """Date the request was sent in Unix time"""

    bio: Optional[str] = None
    """Optional. Bio of the user."""

    invite_link: Optional[ChatInviteLink] = None
    """Optional. Chat invite link that was used by the user to send the join
    request"""

    def adjust(self, bot: Bot):
        self.chat.adjust(bot)
