from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from ..types import (
    InputFile,
    MaskPosition,
    Response
)
from .base import TelegramMethod


@dataclass
class AddStickerToSet(TelegramMethod, response=Response[bool]):
    """
    Use this method to add a new sticker to a set created by the
    bot. You must use exactly one of the fields png_sticker,
    tgs_sticker, or webm_sticker. Animated stickers can be added
    to animated sticker sets and only to them. Animated sticker
    sets can have up to 50 stickers. Static sticker sets can
    have up to 120 stickers. Returns True on success.

    Reference: https://core.telegram.org/bots/api#addstickertoset
    """

    user_id: int
    """User identifier of sticker set owner"""

    name: str
    """Sticker set name"""

    emojis: str
    """One or more emoji corresponding to the sticker"""

    png_sticker: Optional[Union[InputFile, str]] = field(default=None)
    """PNG image with the sticker, must be up to 512 kilobytes in
    size, dimensions must not exceed 512px, and either width or
    height must be exactly 512px. Pass a file_id as a String to
    send a file that already exists on the Telegram servers,
    pass an HTTP URL as a String for Telegram to get a file from
    the Internet, or upload a new one using multipart/form-data.
    More info on Sending Files »"""

    tgs_sticker: Optional[InputFile] = field(default=None)
    """TGS animation with the sticker, uploaded using
    multipart/form-data. See
    https://core.telegram.org/stickers#animated-sticker-
    requirements for technical requirements"""

    webm_sticker: Optional[InputFile] = field(default=None)
    """WEBM video with the sticker, uploaded using multipart/form-
    data. See https://core.telegram.org/stickers#video-sticker-
    requirements for technical requirements"""

    mask_position: Optional[MaskPosition] = field(default=None)
    """A JSON-serialized object for position where the mask should
    be placed on faces"""
