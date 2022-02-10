from __future__ import annotations

from dataclasses import dataclass, field, InitVar
from typing import List, Optional

from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent
from .message_entity import MessageEntity


@dataclass
class InlineQueryResultVoice(InlineQueryResult):
    """
    Represents a link to a voice recording in an .OGG container
    encoded with OPUS. By default, this voice recording will be
    sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified
    content instead of the the voice message.
    Reference: https://core.telegram.org/bots/api#inlinequeryresultvoice
    """

    id: str
    """Unique identifier for this result, 1-64 bytes"""

    voice_url: str
    """A valid URL for the voice recording"""

    title: str
    """Recording title"""

    caption: Optional[str] = field(default=None)
    """Optional. Caption, 0-1024 characters after entities parsing"""

    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the voice message
    caption. See formatting options for more details."""

    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the
    caption, which can be specified instead of parse_mode"""

    voice_duration: Optional[int] = field(default=None)
    """Optional. Recording duration in seconds"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""

    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the
    voice recording"""

    type_: str = field(default='')
    """Type of the result, must be voice"""

    def __post_init__(self):
        self.type_ = "voice"
    