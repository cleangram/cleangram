from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .mask_position import MaskPosition
from .base import TelegramType
from .photo_size import PhotoSize


@dataclass
class Sticker(TelegramType):
    """
    This object represents a sticker.
    Reference: https://core.telegram.org/bots/api#sticker
    """

    file_id: str
    """Identifier for this file, which can be used to download or
    reuse the file"""

    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the
    same over time and for different bots. Can't be used to
    download or reuse the file."""

    width: int
    """Sticker width"""

    height: int
    """Sticker height"""

    is_animated: bool
    """True, if the sticker is animated"""

    thumb: Optional[PhotoSize] = field(default=None)
    """Optional. Sticker thumbnail in the .WEBP or .JPG format"""

    emoji: Optional[str] = field(default=None)
    """Optional. Emoji associated with the sticker"""

    set_name: Optional[str] = field(default=None)
    """Optional. Name of the sticker set to which the sticker
    belongs"""

    mask_position: Optional[MaskPosition] = field(default=None)
    """Optional. For mask stickers, the position where the mask
    should be placed"""

    file_size: Optional[int] = field(default=None)
    """Optional. File size in bytes"""
