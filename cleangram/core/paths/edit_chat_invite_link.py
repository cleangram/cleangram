from typing import Optional, Union

from ...core.objects.response import Response
from ..objects import ChatInviteLink
from .base import TelegramPath


class EditChatInviteLink(TelegramPath, response=Response[ChatInviteLink]):
    """
    Use this method to edit a non-primary invite link created by the bot.
    The bot must be an administrator in the chat for this to work and must
    have the appropriate administrator rights. Returns the edited invite
    link as a ChatInviteLink object.

    Reference: https://core.telegram.org/bots/api#editchatinvitelink
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    channel (in the format @channelusername)"""

    invite_link: str
    """The invite link to edit"""

    name: Optional[str] = None
    """Invite link name; 0-32 characters"""

    expire_date: Optional[int] = None
    """Point in time (Unix timestamp) when the link will expire"""

    member_limit: Optional[int] = None
    """The maximum number of users that can be members of the chat
    simultaneously after joining the chat via this invite link; 1-99999"""

    creates_join_request: Optional[bool] = None
    """True, if users joining the chat via the link need to be approved by
    chat administrators. If True, member_limit can't be specified"""
