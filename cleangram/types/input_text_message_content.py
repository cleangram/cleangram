from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, TYPE_CHECKING

from .input_message_content import InputMessageContent
from .message_entity import MessageEntity


@dataclass
class InputTextMessageContent(InputMessageContent):
    """
    Represents the content of a text message to be sent as the
    result of an inline query.
    Reference: https://core.telegram.org/bots/api#inputtextmessagecontent
    """

    message_text: str
    """Text of the message to be sent, 1-4096 characters"""

    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the message text. See
    formatting options for more details."""

    entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in message
    text, which can be specified instead of parse_mode"""

    disable_web_page_preview: Optional[bool] = field(default=None)
    """Optional. Disables link previews for links in the sent
    message"""
