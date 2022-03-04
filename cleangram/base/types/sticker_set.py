from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from .base import TelegramType
from .photo_size import PhotoSize
from .sticker import Sticker


@dataclass
class StickerSet(TelegramType):
    """
    This object represents a sticker set.
    Reference: https://core.telegram.org/bots/api#stickerset
    """

    name: str
    """Sticker set name"""

    title: str
    """Sticker set title"""

    is_animated: bool
    """True, if the sticker set contains animated stickers"""

    is_video: bool
    """True, if the sticker set contains video stickers"""

    contains_masks: bool
    """True, if the sticker set contains masks"""

    stickers: List[Sticker]
    """List of all set stickers"""

    thumb: Optional[PhotoSize] = field(default=None)
    """Optional. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM
    format"""
