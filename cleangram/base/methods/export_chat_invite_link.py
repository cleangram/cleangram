from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from ..types import Response
from .base import TelegramMethod


@dataclass
class ExportChatInviteLink(TelegramMethod, response=Response[str]):
    """
    Use this method to generate a new primary invite link for a
    chat; any previously generated primary link is revoked. The
    bot must be an administrator in the chat for this to work
    and must have the appropriate administrator rights. Returns
    the new invite link as String on success.

    Reference: https://core.telegram.org/bots/api#exportchatinvitelink
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""
