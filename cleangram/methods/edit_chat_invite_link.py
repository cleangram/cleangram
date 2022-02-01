from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from cleangram.types import (
    Response,
    ChatInviteLink
)
from .base import TelegramMethod


@dataclass
class EditChatInviteLink(TelegramMethod, response=Response[ChatInviteLink]):
    """
    Use this method to edit a non-primary invite link created by
    the bot. The bot must be an administrator in the chat for
    this to work and must have the appropriate administrator
    rights. Returns the edited invite link as a ChatInviteLink
    object.

    Reference: https://core.telegram.org/bots/api#editchatinvitelink
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    invite_link: str
    """The invite link to edit"""

    name: Optional[str] = field(default=None)
    """Invite link name; 0-32 characters"""

    expire_date: Optional[int] = field(default=None)
    """Point in time (Unix timestamp) when the link will expire"""

    member_limit: Optional[int] = field(default=None)
    """Maximum number of users that can be members of the chat
    simultaneously after joining the chat via this invite link;
    1-99999"""

    creates_join_request: Optional[bool] = field(default=None)
    """True, if users joining the chat via the link need to be
    approved by chat administrators. If True, member_limit can't
    be specified"""
