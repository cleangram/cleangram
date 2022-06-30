from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from pydantic import Field

from .inline_query_result import InlineQueryResult

if TYPE_CHECKING:
    from .inline_keyboard_markup import InlineKeyboardMarkup
    from .input_message_content import InputMessageContent
    from .message_entity import MessageEntity


class InlineQueryResultVideo(InlineQueryResult):
    """
    Represents a link to a page containing an embedded video player or a
    video file. By default, this video file will be sent by the user with
    an optional caption. Alternatively, you can use input_message_content
    to send a message with the specified content instead of the video.

    Reference: https://core.telegram.org/bots/api#inlinequeryresultvideo
    """

    id: str
    """Unique identifier for this result, 1-64 bytes"""

    video_url: str
    """A valid URL for the embedded video player or video file"""

    mime_type: str
    """MIME type of the content of the video URL, “text/html” or “video/mp4”"""

    thumb_url: str
    """URL of the thumbnail (JPEG only) for the video"""

    title: str
    """Title for the result"""

    caption: Optional[str] = None
    """Optional. Caption of the video to be sent, 0-1024 characters after
    entities parsing"""

    parse_mode: Optional[str] = None
    """Optional. Mode for parsing entities in the video caption. See
    formatting options for more details."""

    caption_entities: Optional[List[MessageEntity]] = Field(
        default_factory=list
    )
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""

    video_width: Optional[int] = None
    """Optional. Video width"""

    video_height: Optional[int] = None
    """Optional. Video height"""

    video_duration: Optional[int] = None
    """Optional. Video duration in seconds"""

    description: Optional[str] = None
    """Optional. Short description of the result"""

    reply_markup: Optional[InlineKeyboardMarkup] = None
    """Optional. Inline keyboard attached to the message"""

    input_message_content: Optional[InputMessageContent] = None
    """Optional. Content of the message to be sent instead of the video. This
    field is required if InlineQueryResultVideo is used to send an HTML-
    page as a result (e.g., a YouTube video)."""

    type: str = 'video'
    """Type of the result, must be video"""
