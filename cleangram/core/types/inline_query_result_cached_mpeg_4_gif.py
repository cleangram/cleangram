from __future__ import annotations

from dataclasses import dataclass, InitVar, field
from typing import Optional, List

from .inline_keyboard_markup import InlineKeyboardMarkup
from .input_message_content import InputMessageContent
from .message_entity import MessageEntity
from .inline_query_result import InlineQueryResult


@dataclass
class InlineQueryResultCachedMpeg4Gif(InlineQueryResult):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC
    video without sound) stored on the Telegram servers. By
    default, this animated MPEG-4 file will be sent by the user
    with an optional caption. Alternatively, you can use
    input_message_content to send a message with the specified
    content instead of the animation.
    Reference: https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif
    """

    id: str
    """Unique identifier for this result, 1-64 bytes"""

    mpeg4_file_id: str
    """A valid file identifier for the MP4 file"""

    title: Optional[str] = field(default=None)
    """Optional. Title for the result"""

    caption: Optional[str] = field(default=None)
    """Optional. Caption of the MPEG-4 file to be sent, 0-1024
    characters after entities parsing"""

    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the caption. See
    formatting options for more details."""

    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the
    caption, which can be specified instead of parse_mode"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""

    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the
    video animation"""

    type_: str = field(default='mpeg4_gif')
    """Type of the result, must be mpeg4_gif"""
