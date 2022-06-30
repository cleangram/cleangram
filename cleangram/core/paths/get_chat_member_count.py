from typing import Union

from ...core.objects.response import Response
from .base import TelegramPath


class GetChatMemberCount(TelegramPath, response=Response[int]):
    """
    Use this method to get the number of members in a chat. Returns Int on
    success.

    Reference: https://core.telegram.org/bots/api#getchatmembercount
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    supergroup or channel (in the format @channelusername)"""
