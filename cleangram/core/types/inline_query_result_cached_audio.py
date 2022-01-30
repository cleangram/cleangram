from __future__ import annotations

from dataclasses import dataclass, InitVar, field
from typing import Optional, List

from .inline_keyboard_markup import InlineKeyboardMarkup
from .input_message_content import InputMessageContent
from .message_entity import MessageEntity
from .inline_query_result import InlineQueryResult


@dataclass
class InlineQueryResultCachedAudio(InlineQueryResult):
    """
    Represents a link to an MP3 audio file stored on the
    Telegram servers. By default, this audio file will be sent
    by the user. Alternatively, you can use
    input_message_content to send a message with the specified
    content instead of the audio.
    Reference: https://core.telegram.org/bots/api#inlinequeryresultcachedaudio
    """

    id: str
    """Unique identifier for this result, 1-64 bytes"""

    audio_file_id: str
    """A valid file identifier for the audio file"""

    caption: Optional[str] = field(default=None)
    """Optional. Caption, 0-1024 characters after entities parsing"""

    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the audio caption.
    See formatting options for more details."""

    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the
    caption, which can be specified instead of parse_mode"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""

    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the
    audio"""

    type_: str = field(default='audio')
    """Type of the result, must be audio"""
