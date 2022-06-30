from typing import Union

from ...core.objects.response import Response
from .base import TelegramPath


class DeclineChatJoinRequest(TelegramPath, response=Response[bool]):
    """
    Use this method to decline a chat join request. The bot must be an
    administrator in the chat for this to work and must have the
    can_invite_users administrator right. Returns True on success.

    Reference: https://core.telegram.org/bots/api#declinechatjoinrequest
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    channel (in the format @channelusername)"""

    user_id: int
    """Unique identifier of the target user"""
