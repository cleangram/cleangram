from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from cleangram.types import (
    Response
)
from .base import TelegramMethod


@dataclass
class SendChatAction(TelegramMethod, response=Response[bool]):
    """
    Use this method when you need to tell the user that
    something is happening on the bot's side. The status is set
    for 5 seconds or less (when a message arrives from your bot,
    Telegram clients clear its typing status). Returns True on
    success.

    Reference: https://core.telegram.org/bots/api#sendchataction
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    action: str
    """Type of action to broadcast. Choose one, depending on what
    the user is about to receive: typing for text messages,
    upload_photo for photos, record_video or upload_video for
    videos, record_voice or upload_voice for voice notes,
    upload_document for general files, choose_sticker for
    stickers, find_location for location data, record_video_note
    or upload_video_note for video notes."""
