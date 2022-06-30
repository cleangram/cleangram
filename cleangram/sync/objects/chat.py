from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...core import Chat as _Chat

if TYPE_CHECKING:
    from .message import Message


class Chat(_Chat):
    """
    This object represents a chat.

    Reference: https://core.telegram.org/bots/api#chat
    """

    pinned_message: Optional[Message] = None
