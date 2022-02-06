from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from ..types import InputFile, MaskPosition, Response
from .base import TelegramMethod


@dataclass
class CreateNewStickerSet(TelegramMethod, response=Response[bool]):
    """
    Use this method to create a new sticker set owned by a user.
    The bot will be able to edit the sticker set thus created.
    You must use exactly one of the fields png_sticker,
    tgs_sticker, or webm_sticker. Returns True on success.

    Reference: https://core.telegram.org/bots/api#createnewstickerset
    """

    user_id: int
    """User identifier of created sticker set owner"""

    name: str
    """Short name of sticker set, to be used in t.me/addstickers/
    URLs (e.g., animals). Can contain only english letters,
    digits and underscores. Must begin with a letter, can't
    contain consecutive underscores and must end in “_by_<bot
    username>”. <bot_username> is case insensitive. 1-64
    characters."""

    title: str
    """Sticker set title, 1-64 characters"""

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

    contains_masks: Optional[bool] = field(default=None)
    """Pass True, if a set of mask stickers should be created"""

    mask_position: Optional[MaskPosition] = field(default=None)
    """A JSON-serialized object for position where the mask should
    be placed on faces"""
