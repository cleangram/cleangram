from typing import Union

from ...core.objects.response import Response
from .base import TelegramPath


class UnbanChatSenderChat(TelegramPath, response=Response[bool]):
    """
    Use this method to unban a previously banned channel chat in a
    supergroup or channel. The bot must be an administrator for this to
    work and must have the appropriate administrator rights. Returns True
    on success.

    Reference: https://core.telegram.org/bots/api#unbanchatsenderchat
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    channel (in the format @channelusername)"""

    sender_chat_id: int
    """Unique identifier of the target sender chat"""
