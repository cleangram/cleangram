from __future__ import annotations

from dataclasses import dataclass


from ..types import Response, StickerSet
from .base import TelegramMethod


@dataclass
class GetStickerSet(TelegramMethod, response=Response[StickerSet]):
    """
    Use this method to get a sticker set. On success, a
    StickerSet object is returned.

    Reference: https://core.telegram.org/bots/api#getstickerset
    """

    name: str
    """Name of the sticker set"""
