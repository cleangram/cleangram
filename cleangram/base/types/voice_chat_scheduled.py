from __future__ import annotations

from dataclasses import dataclass

from .base import TelegramType


@dataclass
class VoiceChatScheduled(TelegramType):
    """
    This object represents a service message about a voice chat
    scheduled in the chat.
    Reference: https://core.telegram.org/bots/api#voicechatscheduled
    """

    start_date: int
    """Point in time (Unix timestamp) when the voice chat is
    supposed to be started by a chat administrator"""
