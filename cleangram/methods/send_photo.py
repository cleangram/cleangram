from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Union

from ..types import (
    ForceReply,
    InlineKeyboardMarkup,
    InputFile,
    Message,
    MessageEntity,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Response
)
from .base import TelegramMethod


@dataclass
class SendPhoto(TelegramMethod, response=Response[Message]):
    """
    Use this method to send photos. On success, the sent Message
    is returned.

    Reference: https://core.telegram.org/bots/api#sendphoto
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    photo: Union[InputFile, str]
    """Photo to send. Pass a file_id as String to send a photo that
    exists on the Telegram servers (recommended), pass an HTTP
    URL as a String for Telegram to get a photo from the
    Internet, or upload a new photo using multipart/form-data.
    The photo must be at most 10 MB in size. The photo's width
    and height must not exceed 10000 in total. Width and height
    ratio must be at most 20. More info on Sending Files »"""

    caption: Optional[str] = field(default=None)
    """Photo caption (may also be used when resending photos by
    file_id), 0-1024 characters after entities parsing"""

    parse_mode: Optional[str] = field(default=None)
    """Mode for parsing entities in the photo caption. See
    formatting options for more details."""

    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """A JSON-serialized list of special entities that appear in
    the caption, which can be specified instead of parse_mode"""

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
