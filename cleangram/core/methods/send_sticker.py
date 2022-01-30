from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from ..types import (
    Response,
    InputFile,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    Message,
    ForceReply
)
from .base import TelegramMethod


@dataclass
class SendSticker(TelegramMethod, response=Response[Message]):
    """
    Use this method to send static .WEBP or animated .TGS
    stickers. On success, the sent Message is returned.

    Reference: https://core.telegram.org/bots/api#sendsticker
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    sticker: Union[InputFile, str]
    """Sticker to send. Pass a file_id as String to send a file
    that exists on the Telegram servers (recommended), pass an
    HTTP URL as a String for Telegram to get a .WEBP file from
    the Internet, or upload a new one using multipart/form-data.
    More info on Sending Files »"""

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
