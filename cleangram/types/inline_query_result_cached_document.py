from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, TYPE_CHECKING

from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent
from .message_entity import MessageEntity


@dataclass
class InlineQueryResultCachedDocument(InlineQueryResult):
    """
    Represents a link to a file stored on the Telegram servers.
    By default, this file will be sent by the user with an
    optional caption. Alternatively, you can use
    input_message_content to send a message with the specified
    content instead of the file.
    Reference: https://core.telegram.org/bots/api#inlinequeryresultcacheddocument
    """

    id: str
    """Unique identifier for this result, 1-64 bytes"""

    title: str
    """Title for the result"""

    document_file_id: str
    """A valid file identifier for the file"""

    description: Optional[str] = field(default=None)
    """Optional. Short description of the result"""

    caption: Optional[str] = field(default=None)
    """Optional. Caption of the document to be sent, 0-1024
    characters after entities parsing"""

    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the document caption.
    See formatting options for more details."""

    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the
    caption, which can be specified instead of parse_mode"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""

    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the
    file"""

    type_: str = field(default="")
    """Type of the result, must be document"""

    def __post_init__(self):
        self.type_ = "document"
