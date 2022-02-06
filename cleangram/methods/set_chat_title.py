from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from ..types import Response
from .base import TelegramMethod


@dataclass
class SetChatTitle(TelegramMethod, response=Response[bool]):
    """
    Use this method to change the title of a chat. Titles can't
    be changed for private chats. The bot must be an
    administrator in the chat for this to work and must have the
    appropriate administrator rights. Returns True on success.

    Reference: https://core.telegram.org/bots/api#setchattitle
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    title: str
    """New chat title, 1-255 characters"""
