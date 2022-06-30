from typing import Union

from ...core.objects.response import Response
from .base import TelegramPath


class LeaveChat(TelegramPath, response=Response[bool]):
    """
    Use this method for your bot to leave a group, supergroup or channel.
    Returns True on success.

    Reference: https://core.telegram.org/bots/api#leavechat
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    supergroup or channel (in the format @channelusername)"""
