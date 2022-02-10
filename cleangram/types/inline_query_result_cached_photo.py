from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, TYPE_CHECKING

from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent
from .message_entity import MessageEntity


@dataclass
class InlineQueryResultCachedPhoto(InlineQueryResult):
    """
    Represents a link to a photo stored on the Telegram servers.
    By default, this photo will be sent by the user with an
    optional caption. Alternatively, you can use
    input_message_content to send a message with the specified
    content instead of the photo.
    Reference: https://core.telegram.org/bots/api#inlinequeryresultcachedphoto
    """

    id: str
    """Unique identifier for this result, 1-64 bytes"""

    photo_file_id: str
    """A valid file identifier of the photo"""

    title: Optional[str] = field(default=None)
    """Optional. Title for the result"""

    description: Optional[str] = field(default=None)
    """Optional. Short description of the result"""

    caption: Optional[str] = field(default=None)
    """Optional. Caption of the photo to be sent, 0-1024 characters
    after entities parsing"""

    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the photo caption.
    See formatting options for more details."""

    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the
    caption, which can be specified instead of parse_mode"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""

    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the
    photo"""

    type_: str = field(default="")
    """Type of the result, must be photo"""

    def __post_init__(self):
        self.type_ = "photo"
