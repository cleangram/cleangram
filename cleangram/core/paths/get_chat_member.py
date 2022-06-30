from typing import Union

from ...core.objects.response import Response
from ..objects import ChatMember
from .base import TelegramPath


class GetChatMember(TelegramPath, response=Response[ChatMember]):
    """
    Use this method to get information about a member of a chat. Returns a
    ChatMember object on success.

    Reference: https://core.telegram.org/bots/api#getchatmember
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    supergroup or channel (in the format @channelusername)"""

    user_id: int
    """Unique identifier of the target user"""
