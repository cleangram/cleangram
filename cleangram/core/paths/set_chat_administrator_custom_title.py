from typing import Union

from ...core.objects.response import Response
from .base import TelegramPath


class SetChatAdministratorCustomTitle(TelegramPath, response=Response[bool]):
    """
    Use this method to set a custom title for an administrator in a
    supergroup promoted by the bot. Returns True on success.

    Reference: https://core.telegram.org/bots/api#setchatadministratorcustomtitle
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    supergroup (in the format @supergroupusername)"""

    user_id: int
    """Unique identifier of the target user"""

    custom_title: str
    """New custom title for the administrator; 0-16 characters, emoji are not
    allowed"""
