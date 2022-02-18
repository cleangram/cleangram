from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union

from ..types import (
    ForceReply,
    InlineKeyboardMarkup,
    InputFile,
    Message,
    MessageEntity,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Response,
)
from .base import TelegramMethod

from ...utils import Presets, attach


@dataclass
class SendAnimation(TelegramMethod, response=Response[Message]):
    """
    Use this method to send animation files (GIF or H.264/MPEG-4
    AVC video without sound). On success, the sent Message is
    returned. Bots can currently send animation files of up to
    50 MB in size, this limit may be changed in the future.

    Reference: https://core.telegram.org/bots/api#sendanimation
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    animation: Union[InputFile, str]
    """Animation to send. Pass a file_id as String to send an
    animation that exists on the Telegram servers (recommended),
    pass an HTTP URL as a String for Telegram to get an
    animation from the Internet, or upload a new animation using
    multipart/form-data. More info on Sending Files »"""

    duration: Optional[int] = field(default=None)
    """Duration of sent animation in seconds"""

    width: Optional[int] = field(default=None)
    """Animation width"""

    height: Optional[int] = field(default=None)
    """Animation height"""

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
    """Animation caption (may also be used when resending animation
    by file_id), 0-1024 characters after entities parsing"""

    parse_mode: Optional[str] = field(default=None)
    """Mode for parsing entities in the animation caption. See
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

    reply_markup: Optional[
        Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ]
    ] = field(default=None)
    """Additional interface options. A JSON-serialized object for
    an inline keyboard, custom reply keyboard, instructions to
    remove reply keyboard or to force a reply from the user."""

    def preset(self, presets: Presets) -> Dict[str, InputFile]:
        presets.parse_mode(self)
        presets.disable_notification(self)
        presets.protect_content(self)
        presets.allow_sending_without_reply(self)
        files = super(SendAnimation, self).preset(presets)
        self.animation = attach(self.animation, files)
        self.thumb = attach(self.thumb, files)
        return files
