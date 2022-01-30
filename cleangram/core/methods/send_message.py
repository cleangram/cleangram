from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, List, Union

from ..types import (
    Response,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    MessageEntity,
    Message,
    ForceReply
)
from .base import TelegramMethod


@dataclass
class SendMessage(TelegramMethod, response=Response[Message]):
    """
    Use this method to send text messages. On success, the sent
    Message is returned.

    Reference: https://core.telegram.org/bots/api#sendmessage
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    text: str
    """Text of the message to be sent, 1-4096 characters after
    entities parsing"""

    parse_mode: Optional[str] = field(default=None)
    """Mode for parsing entities in the message text. See
    formatting options for more details."""

    entities: Optional[List[MessageEntity]] = field(default=None)
    """A JSON-serialized list of special entities that appear in
    message text, which can be specified instead of parse_mode"""

    disable_web_page_preview: Optional[bool] = field(default=None)
    """Disables link previews for links in this message"""

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
    remove reply keyboard or to force a reply from the user."""
