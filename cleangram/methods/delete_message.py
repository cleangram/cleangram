from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from ..types import (
    Response
)
from .base import TelegramMethod


@dataclass
class DeleteMessage(TelegramMethod, response=Response[bool]):
    """
    Use this method to delete a message, including service
    messages, with the following limitations:- A message can
    only be deleted if it was sent less than 48 hours ago.- A
    dice message in a private chat can only be deleted if it was
    sent more than 24 hours ago.- Bots can delete outgoing
    messages in private chats, groups, and supergroups.- Bots
    can delete incoming messages in private chats.- Bots granted
    can_post_messages permissions can delete outgoing messages
    in channels.- If the bot is an administrator of a group, it
    can delete any message there.- If the bot has
    can_delete_messages permission in a supergroup or a channel,
    it can delete any message there.Returns True on success.

    Reference: https://core.telegram.org/bots/api#deletemessage
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    message_id: int
    """Identifier of the message to delete"""
