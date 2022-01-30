from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from ..types import (
    Response,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    Message,
    ForceReply
)
from .base import TelegramMethod


@dataclass
class SendContact(TelegramMethod, response=Response[Message]):
    """
    Use this method to send phone contacts. On success, the sent
    Message is returned.

    Reference: https://core.telegram.org/bots/api#sendcontact
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    phone_number: str
    """Contact's phone number"""

    first_name: str
    """Contact's first name"""

    last_name: Optional[str] = field(default=None)
    """Contact's last name"""

    vcard: Optional[str] = field(default=None)
    """Additional data about the contact in the form of a vCard,
    0-2048 bytes"""

    disable_notification: Optional[bool] = field(default=None)
    """Sends the message silently. Users will receive a
    notification with no sound."""

    protect_content: Optional[bool] = field(default=None)
    """Protects the contents of the sent message from forwarding
    and saving"""

    reply_to_message_id: Optional[int] = field(default=None)
    """If the message is a reply, ID of the original message"""

    allow_sending_without_reply: Optional[bool] = field(default=None)
    """Pass True, if the message should be sent even if the
    specified replied-to message is not found"""

    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = field(default=None)
    """Additional interface options. A JSON-serialized object for
    an inline keyboard, custom reply keyboard, instructions to
    remove keyboard or to force a reply from the user."""
