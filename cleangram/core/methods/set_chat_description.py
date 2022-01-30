from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from ..types import (
    Response
)
from .base import TelegramMethod


@dataclass
class SetChatDescription(TelegramMethod, response=Response[bool]):
    """
    Use this method to change the description of a group, a
    supergroup or a channel. The bot must be an administrator in
    the chat for this to work and must have the appropriate
    administrator rights. Returns True on success.

    Reference: https://core.telegram.org/bots/api#setchatdescription
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    description: Optional[str] = field(default=None)
    """New chat description, 0-255 characters"""
