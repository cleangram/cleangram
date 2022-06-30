from typing import Union

from ...core.objects.response import Response
from .base import TelegramPath


class ExportChatInviteLink(TelegramPath, response=Response[str]):
    """
    Use this method to generate a new primary invite link for a chat; any
    previously generated primary link is revoked. The bot must be an
    administrator in the chat for this to work and must have the
    appropriate administrator rights. Returns the new invite link as
    String on success.

    Reference: https://core.telegram.org/bots/api#exportchatinvitelink
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    channel (in the format @channelusername)"""
