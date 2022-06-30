from __future__ import annotations

from typing import TYPE_CHECKING

from ...core import ChatJoinRequest as _ChatJoinRequest

if TYPE_CHECKING:
    from .chat import Chat


class ChatJoinRequest(_ChatJoinRequest):
    """
    Represents a join request sent to a chat.

    Reference: https://core.telegram.org/bots/api#chatjoinrequest
    """

    chat: Chat
