from __future__ import annotations

from dataclasses import dataclass


from cleangram.types import (
    Response
)
from .base import TelegramMethod


@dataclass
class SetStickerPositionInSet(TelegramMethod, response=Response[bool]):
    """
    Use this method to move a sticker in a set created by the
    bot to a specific position. Returns True on success.

    Reference: https://core.telegram.org/bots/api#setstickerpositioninset
    """

    sticker: str
    """File identifier of the sticker"""

    position: int
    """New sticker position in the set, zero-based"""
