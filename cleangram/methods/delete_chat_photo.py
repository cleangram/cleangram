from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from ..types import (
    Response
)
from .base import TelegramMethod


@dataclass
class DeleteChatPhoto(TelegramMethod, response=Response[bool]):
    """
    Use this method to delete a chat photo. Photos can't be
    changed for private chats. The bot must be an administrator
    in the chat for this to work and must have the appropriate
    administrator rights. Returns True on success.

    Reference: https://core.telegram.org/bots/api#deletechatphoto
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""
