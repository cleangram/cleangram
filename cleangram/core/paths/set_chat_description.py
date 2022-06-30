from typing import Optional, Union

from ...core.objects.response import Response
from .base import TelegramPath


class SetChatDescription(TelegramPath, response=Response[bool]):
    """
    Use this method to change the description of a group, a supergroup or
    a channel. The bot must be an administrator in the chat for this to
    work and must have the appropriate administrator rights. Returns True
    on success.

    Reference: https://core.telegram.org/bots/api#setchatdescription
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    channel (in the format @channelusername)"""

    description: Optional[str] = None
    """New chat description, 0-255 characters"""
