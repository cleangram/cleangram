from __future__ import annotations

from .base import TelegramObject


class VideoChatScheduled(TelegramObject):
    """
    This object represents a service message about a video chat scheduled
    in the chat.

    Reference: https://core.telegram.org/bots/api#videochatscheduled
    """

    start_date: int
    """Point in time (Unix timestamp) when the video chat is supposed to be
    started by a chat administrator"""
