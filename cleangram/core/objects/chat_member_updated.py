from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Optional

from pydantic import Field

from ..bot.bot import Bot
from .base import TelegramObject

if TYPE_CHECKING:
    from .chat import Chat
    from .chat_invite_link import ChatInviteLink
    from .chat_member import ChatMember
    from .user import User


class ChatMemberUpdated(TelegramObject, abc.ABC):
    """
    This object represents changes in the status of a chat member.

    Reference: https://core.telegram.org/bots/api#chatmemberupdated
    """

    chat: Chat
    """Chat the user belongs to"""

    from_: User = Field(alias='from')
    """Performer of the action, which resulted in the change"""

    date: int
    """Date the change was done in Unix time"""

    old_chat_member: ChatMember
    """Previous information about the chat member"""

    new_chat_member: ChatMember
    """New information about the chat member"""

    invite_link: Optional[ChatInviteLink] = None
    """Optional. Chat invite link, which was used by the user to join the
    chat; for joining by invite link events only."""

    def adjust(self, bot: Bot):
        self.chat.adjust(bot)
