from __future__ import annotations

from dataclasses import dataclass, field, InitVar
from typing import List, Optional

from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent
from .message_entity import MessageEntity


@dataclass
class InlineQueryResultDocument(InlineQueryResult):
    """
    Represents a link to a file. By default, this file will be
    sent by the user with an optional caption. Alternatively,
    you can use input_message_content to send a message with the
    specified content instead of the file. Currently, only .PDF
    and .ZIP files can be sent using this method.
    Reference: https://core.telegram.org/bots/api#inlinequeryresultdocument
    """

    id: str
    """Unique identifier for this result, 1-64 bytes"""

    title: str
    """Title for the result"""

    document_url: str
    """A valid URL for the file"""

    mime_type: str
    """Mime type of the content of the file, either
    “application/pdf” or “application/zip”"""

    caption: Optional[str] = field(default=None)
    """Optional. Caption of the document to be sent, 0-1024
    characters after entities parsing"""

    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the document caption.
    See formatting options for more details."""

    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the
    caption, which can be specified instead of parse_mode"""

    description: Optional[str] = field(default=None)
    """Optional. Short description of the result"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""

    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the
    file"""

    thumb_url: Optional[str] = field(default=None)
    """Optional. URL of the thumbnail (JPEG only) for the file"""

    thumb_width: Optional[int] = field(default=None)
    """Optional. Thumbnail width"""

    thumb_height: Optional[int] = field(default=None)
    """Optional. Thumbnail height"""

    type_: str = field(default='document')
    """Type of the result, must be document"""
