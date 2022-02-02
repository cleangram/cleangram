from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from ..types import (
    Response
)
from .base import TelegramMethod


@dataclass
class DeleteChatStickerSet(TelegramMethod, response=Response[bool]):
    """
    Use this method to delete a group sticker set from a
    supergroup. The bot must be an administrator in the chat for
    this to work and must have the appropriate administrator
    rights. Use the field can_set_sticker_set optionally
    returned in getChat requests to check if the bot can use
    this method. Returns True on success.

    Reference: https://core.telegram.org/bots/api#deletechatstickerset
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target supergroup (in the format @supergroupusername)"""
