from __future__ import annotations

from dataclasses import dataclass


from .base import TelegramType


@dataclass
class VoiceChatStarted(TelegramType):
    """
    This object represents a service message about a voice chat
    started in the chat. Currently holds no information.
    Reference: https://core.telegram.org/bots/api#voicechatstarted
    """
