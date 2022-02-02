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
class SendVideo(TelegramMethod, response=Response[Message]):
    """
    Use this method to send video files, Telegram clients
    support mp4 videos (other formats may be sent as Document).
    On success, the sent Message is returned. Bots can currently
    send video files of up to 50 MB in size, this limit may be
    changed in the future.

    Reference: https://core.telegram.org/bots/api#sendvideo
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    video: Union[InputFile, str]
    """Video to send. Pass a file_id as String to send a video that
    exists on the Telegram servers (recommended), pass an HTTP
    URL as a String for Telegram to get a video from the
    Internet, or upload a new video using multipart/form-data.
    More info on Sending Files »"""

    duration: Optional[int] = field(default=None)
    """Duration of sent video in seconds"""

    width: Optional[int] = field(default=None)
    """Video width"""

    height: Optional[int] = field(default=None)
    """Video height"""

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

    caption: Optional[str] = field(default=None)
    """Video caption (may also be used when resending videos by
    file_id), 0-1024 characters after entities parsing"""

    parse_mode: Optional[str] = field(default=None)
    """Mode for parsing entities in the video caption. See
    formatting options for more details."""

    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """A JSON-serialized list of special entities that appear in
    the caption, which can be specified instead of parse_mode"""

    supports_streaming: Optional[bool] = field(default=None)
    """Pass True, if the uploaded video is suitable for streaming"""

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
