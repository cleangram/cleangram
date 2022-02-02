from __future__ import annotations

from dataclasses import dataclass, field, InitVar
from typing import Optional

from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent


@dataclass
class InlineQueryResultContact(InlineQueryResult):
    """
    Represents a contact with a phone number. By default, this
    contact will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified
    content instead of the contact.
    Reference: https://core.telegram.org/bots/api#inlinequeryresultcontact
    """

    id: str
    """Unique identifier for this result, 1-64 Bytes"""

    phone_number: str
    """Contact's phone number"""

    first_name: str
    """Contact's first name"""

    last_name: Optional[str] = field(default=None)
    """Optional. Contact's last name"""

    vcard: Optional[str] = field(default=None)
    """Optional. Additional data about the contact in the form of a
    vCard, 0-2048 bytes"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""

    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the
    contact"""

    thumb_url: Optional[str] = field(default=None)
    """Optional. Url of the thumbnail for the result"""

    thumb_width: Optional[int] = field(default=None)
    """Optional. Thumbnail width"""

    thumb_height: Optional[int] = field(default=None)
    """Optional. Thumbnail height"""

    type_: str = field(default='contact')
    """Type of the result, must be contact"""
