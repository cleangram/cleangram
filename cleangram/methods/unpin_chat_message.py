from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from cleangram.types import (
    Response
)
from .base import TelegramMethod


@dataclass
class UnpinChatMessage(TelegramMethod, response=Response[bool]):
    """
    Use this method to remove a message from the list of pinned
    messages in a chat. If the chat is not a private chat, the
    bot must be an administrator in the chat for this to work
    and must have the 'can_pin_messages' administrator right in
    a supergroup or 'can_edit_messages' administrator right in a
    channel. Returns True on success.

    Reference: https://core.telegram.org/bots/api#unpinchatmessage
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    message_id: Optional[int] = field(default=None)
    """Identifier of a message to unpin. If not specified, the most
    recent pinned message (by sending date) will be unpinned."""
