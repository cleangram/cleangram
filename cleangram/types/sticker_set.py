from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, List

from .sticker import Sticker
from .base import TelegramType
from .photo_size import PhotoSize


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

    contains_masks: bool
    """True, if the sticker set contains masks"""

    stickers: List[Sticker]
    """List of all set stickers"""

    thumb: Optional[PhotoSize] = field(default=None)
    """Optional. Sticker set thumbnail in the .WEBP or .TGS format"""
