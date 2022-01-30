from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .base import TelegramType


@dataclass
class ChatPermissions(TelegramType):
    """
    Describes actions that a non-administrator user is allowed
    to take in a chat.
    Reference: https://core.telegram.org/bots/api#chatpermissions
    """

    can_send_messages: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to send text
    messages, contacts, locations and venues"""

    can_send_media_messages: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to send audios,
    documents, photos, videos, video notes and voice notes,
    implies can_send_messages"""

    can_send_polls: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to send polls,
    implies can_send_messages"""

    can_send_other_messages: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to send animations,
    games, stickers and use inline bots, implies
    can_send_media_messages"""

    can_add_web_page_previews: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to add web page
    previews to their messages, implies can_send_media_messages"""

    can_change_info: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to change the chat
    title, photo and other settings. Ignored in public
    supergroups"""

    can_invite_users: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to invite new users
    to the chat"""

    can_pin_messages: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to pin messages.
    Ignored in public supergroups"""
