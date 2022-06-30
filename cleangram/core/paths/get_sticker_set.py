from ...core.objects.response import Response
from ..objects import StickerSet
from .base import TelegramPath


class GetStickerSet(TelegramPath, response=Response[StickerSet]):
    """
    Use this method to get a sticker set. On success, a StickerSet object
    is returned.

    Reference: https://core.telegram.org/bots/api#getstickerset
    """

    name: str
    """Name of the sticker set"""
