from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent


@dataclass
class InlineQueryResultCachedSticker(InlineQueryResult):
    """
    Represents a link to a sticker stored on the Telegram
    servers. By default, this sticker will be sent by the user.
    Alternatively, you can use input_message_content to send a
    message with the specified content instead of the sticker.
    Reference: https://core.telegram.org/bots/api#inlinequeryresultcachedsticker
    """

    id: str
    """Unique identifier for this result, 1-64 bytes"""

    sticker_file_id: str
    """A valid file identifier of the sticker"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""

    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the
    sticker"""

    type_: str = field(default="")
    """Type of the result, must be sticker"""

    def __post_init__(self):
        self.type_ = "sticker"
