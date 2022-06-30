from ...core.objects.response import Response
from .base import TelegramPath


class DeleteStickerFromSet(TelegramPath, response=Response[bool]):
    """
    Use this method to delete a sticker from a set created by the bot.
    Returns True on success.

    Reference: https://core.telegram.org/bots/api#deletestickerfromset
    """

    sticker: str
    """File identifier of the sticker"""
