from typing import Optional, Union

from ...core.objects.response import Response
from ..objects import ChatPermissions
from .base import TelegramPath


class RestrictChatMember(TelegramPath, response=Response[bool]):
    """
    Use this method to restrict a user in a supergroup. The bot must be an
    administrator in the supergroup for this to work and must have the
    appropriate administrator rights. Pass True for all permissions to
    lift restrictions from a user. Returns True on success.

    Reference: https://core.telegram.org/bots/api#restrictchatmember
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    supergroup (in the format @supergroupusername)"""

    user_id: int
    """Unique identifier of the target user"""

    permissions: ChatPermissions
    """A JSON-serialized object for new user permissions"""

    until_date: Optional[int] = None
    """Date when restrictions will be lifted for the user, unix time. If user
    is restricted for more than 366 days or less than 30 seconds from the
    current time, they are considered to be restricted forever"""
