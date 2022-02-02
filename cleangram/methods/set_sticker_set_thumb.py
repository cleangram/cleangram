from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from ..types import (
    InputFile,
    Response
)
from .base import TelegramMethod


@dataclass
class SetStickerSetThumb(TelegramMethod, response=Response[bool]):
    """
    Use this method to set the thumbnail of a sticker set.
    Animated thumbnails can be set for animated sticker sets
    only. Video thumbnails can be set only for video sticker
    sets only. Returns True on success.

    Reference: https://core.telegram.org/bots/api#setstickersetthumb
    """

    name: str
    """Sticker set name"""

    user_id: int
    """User identifier of the sticker set owner"""

    thumb: Optional[Union[InputFile, str]] = field(default=None)
    """A PNG image with the thumbnail, must be up to 128 kilobytes
    in size and have width and height exactly 100px, or a TGS
    animation with the thumbnail up to 32 kilobytes in size; see
    https://core.telegram.org/stickers#animated-sticker-
    requirements for animated sticker technical requirements, or
    a WEBM video with the thumbnail up to 32 kilobytes in size;
    see https://core.telegram.org/stickers#video-sticker-
    requirements for video sticker technical requirements. Pass
    a file_id as a String to send a file that already exists on
    the Telegram servers, pass an HTTP URL as a String for
    Telegram to get a file from the Internet, or upload a new
    one using multipart/form-data. More info on Sending Files ».
    Animated sticker set thumbnails can't be uploaded via HTTP
    URL."""
