from __future__ import annotations

from dataclasses import dataclass


from ..types import Response
from .base import TelegramMethod


@dataclass
class DeleteStickerFromSet(TelegramMethod, response=Response[bool]):
    """
    Use this method to delete a sticker from a set created by
    the bot. Returns True on success.

    Reference: https://core.telegram.org/bots/api#deletestickerfromset
    """

    sticker: str
    """File identifier of the sticker"""
