from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent


@dataclass
class InlineQueryResultArticle(InlineQueryResult):
    """
    Represents a link to an article or web page.
    Reference: https://core.telegram.org/bots/api#inlinequeryresultarticle
    """

    id: str
    """Unique identifier for this result, 1-64 Bytes"""

    title: str
    """Title of the result"""

    input_message_content: InputMessageContent
    """Content of the message to be sent"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""

    url: Optional[str] = field(default=None)
    """Optional. URL of the result"""

    hide_url: Optional[bool] = field(default=None)
    """Optional. Pass True, if you don't want the URL to be shown
    in the message"""

    description: Optional[str] = field(default=None)
    """Optional. Short description of the result"""

    thumb_url: Optional[str] = field(default=None)
    """Optional. Url of the thumbnail for the result"""

    thumb_width: Optional[int] = field(default=None)
    """Optional. Thumbnail width"""

    thumb_height: Optional[int] = field(default=None)
    """Optional. Thumbnail height"""

    type_: str = field(default="")
    """Type of the result, must be article"""

    def __post_init__(self):
        self.type_ = "article"
