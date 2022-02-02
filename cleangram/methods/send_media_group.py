from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Union

from ..types import (
    InputMediaAudio,
    InputMediaDocument,
    InputMediaPhoto,
    InputMediaVideo,
    Message,
    Response
)
from .base import TelegramMethod


@dataclass
class SendMediaGroup(TelegramMethod, response=Response[List[Message]]):
    """
    Use this method to send a group of photos, videos, documents
    or audios as an album. Documents and audio files can be only
    grouped in an album with messages of the same type. On
    success, an array of Messages that were sent is returned.

    Reference: https://core.telegram.org/bots/api#sendmediagroup
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    media: List[Union[InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo]]
    """A JSON-serialized array describing messages to be sent, must
    include 2-10 items"""

    disable_notification: Optional[bool] = field(default=None)
    """Sends messages silently. Users will receive a notification
    with no sound."""

    protect_content: Optional[bool] = field(default=None)
    """Protects the contents of the sent messages from forwarding
    and saving"""

    reply_to_message_id: Optional[int] = field(default=None)
    """If the messages are a reply, ID of the original message"""

    allow_sending_without_reply: Optional[bool] = field(default=None)
    """Pass True, if the message should be sent even if the
    specified replied-to message is not found"""
