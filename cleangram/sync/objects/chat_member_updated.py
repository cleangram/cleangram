from __future__ import annotations

from typing import TYPE_CHECKING

from ...core import ChatMemberUpdated as _ChatMemberUpdated

if TYPE_CHECKING:
    from .chat import Chat


class ChatMemberUpdated(_ChatMemberUpdated):
    """
    This object represents changes in the status of a chat member.

    Reference: https://core.telegram.org/bots/api#chatmemberupdated
    """

    chat: Chat
