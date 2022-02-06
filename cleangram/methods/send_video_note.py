from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from ..types import (
    ForceReply,
    InlineKeyboardMarkup,
    InputFile,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Response,
)
from .base import TelegramMethod


@dataclass
class SendVideoNote(TelegramMethod, response=Response[Message]):
    """
    As of v.4.0, Telegram clients support rounded square mp4
    videos of up to 1 minute long. Use this method to send video
    messages. On success, the sent Message is returned.

    Reference: https://core.telegram.org/bots/api#sendvideonote
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    video_note: Union[InputFile, str]
    """Video note to send. Pass a file_id as String to send a video
    note that exists on the Telegram servers (recommended) or
    upload a new video using multipart/form-data. More info on
    Sending Files ». Sending video notes by a URL is currently
    unsupported"""

    duration: Optional[int] = field(default=None)
    """Duration of sent video in seconds"""

    length: Optional[int] = field(default=None)
    """Video width and height, i.e. diameter of the video message"""

    thumb: Optional[Union[InputFile, str]] = field(default=None)
    """Thumbnail of the file sent; can be ignored if thumbnail
    generation for the file is supported server-side. The
    thumbnail should be in JPEG format and less than 200 kB in
    size. A thumbnail's width and height should not exceed 320.
    Ignored if the file is not uploaded using multipart/form-
    data. Thumbnails can't be reused and can be only uploaded as
    a new file, so you can pass “attach://<file_attach_name>” if
    the thumbnail was uploaded using multipart/form-data under
    <file_attach_name>. More info on Sending Files »"""

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

    reply_markup: Optional[
        Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ]
    ] = field(default=None)
    """Additional interface options. A JSON-serialized object for
    an inline keyboard, custom reply keyboard, instructions to
    remove reply keyboard or to force a reply from the user."""
