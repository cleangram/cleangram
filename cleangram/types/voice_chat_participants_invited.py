from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from .base import TelegramType
from .user import User


@dataclass
class VoiceChatParticipantsInvited(TelegramType):
    """
    This object represents a service message about new members
    invited to a voice chat.
    Reference: https://core.telegram.org/bots/api#voicechatparticipantsinvited
    """

    users: Optional[List[User]] = field(default=None)
    """Optional. New members that were invited to the voice chat"""
