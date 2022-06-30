from typing import Optional

from ...core.objects.response import Response
from ..objects import ChatAdministratorRights
from .base import TelegramPath


class GetMyDefaultAdministratorRights(
    TelegramPath, response=Response[ChatAdministratorRights]
):
    """
    Use this method to get the current default administrator rights of the
    bot. Returns ChatAdministratorRights on success.

    Reference: https://core.telegram.org/bots/api#getmydefaultadministratorrights
    """

    for_channels: Optional[bool] = None
    """Pass True to get default administrator rights of the bot in channels.
    Otherwise, default administrator rights of the bot for groups and
    supergroups will be returned."""
