from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, TYPE_CHECKING

from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent
from .message_entity import MessageEntity


@dataclass
class InlineQueryResultAudio(InlineQueryResult):
    """
    Represents a link to an MP3 audio file. By default, this
    audio file will be sent by the user. Alternatively, you can
    use input_message_content to send a message with the
    specified content instead of the audio.
    Reference: https://core.telegram.org/bots/api#inlinequeryresultaudio
    """

    id: str
    """Unique identifier for this result, 1-64 bytes"""

    audio_url: str
    """A valid URL for the audio file"""

    title: str
    """Title"""

    caption: Optional[str] = field(default=None)
    """Optional. Caption, 0-1024 characters after entities parsing"""

    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the audio caption.
    See formatting options for more details."""

    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the
    caption, which can be specified instead of parse_mode"""

    performer: Optional[str] = field(default=None)
    """Optional. Performer"""

    audio_duration: Optional[int] = field(default=None)
    """Optional. Audio duration in seconds"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""

    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the
    audio"""

    type_: str = field(default="")
    """Type of the result, must be audio"""

    def __post_init__(self):
        self.type_ = "audio"
