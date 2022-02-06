from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from ..types import ChatInviteLink, Response
from .base import TelegramMethod


@dataclass
class RevokeChatInviteLink(TelegramMethod, response=Response[ChatInviteLink]):
    """
    Use this method to revoke an invite link created by the bot.
    If the primary link is revoked, a new link is automatically
    generated. The bot must be an administrator in the chat for
    this to work and must have the appropriate administrator
    rights. Returns the revoked invite link as ChatInviteLink
    object.

    Reference: https://core.telegram.org/bots/api#revokechatinvitelink
    """

    chat_id: Union[str, int]
    """Unique identifier of the target chat or username of the
    target channel (in the format @channelusername)"""

    invite_link: str
    """The invite link to revoke"""
