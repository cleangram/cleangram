from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from pydantic import Field

from .base import TelegramObject

if TYPE_CHECKING:
    from .photo_size import PhotoSize
    from .sticker import Sticker


class StickerSet(TelegramObject):
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

    stickers: List[Sticker] = Field(default_factory=list)
    """List of all set stickers"""

    thumb: Optional[PhotoSize] = None
    """Optional. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format"""
