from __future__ import annotations

from dataclasses import dataclass


from .base import TelegramType


@dataclass
class VoiceChatEnded(TelegramType):
    """
    This object represents a service message about a voice chat
    ended in the chat.
    Reference: https://core.telegram.org/bots/api#voicechatended
    """

    duration: int
    """Voice chat duration in seconds"""
