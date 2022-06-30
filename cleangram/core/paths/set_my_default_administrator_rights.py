from typing import Optional

from ...core.objects.response import Response
from ..objects import ChatAdministratorRights
from .base import TelegramPath


class SetMyDefaultAdministratorRights(TelegramPath, response=Response[bool]):
    """
    Use this method to change the default administrator rights requested
    by the bot when it's added as an administrator to groups or channels.
    These rights will be suggested to users, but they are are free to
    modify the list before adding the bot. Returns True on success.

    Reference: https://core.telegram.org/bots/api#setmydefaultadministratorrights
    """

    rights: Optional[ChatAdministratorRights] = None
    """A JSON-serialized object describing new default administrator rights.
    If not specified, the default administrator rights will be cleared."""

    for_channels: Optional[bool] = None
    """Pass True to change the default administrator rights of the bot in
    channels. Otherwise, the default administrator rights of the bot for
    groups and supergroups will be changed."""
