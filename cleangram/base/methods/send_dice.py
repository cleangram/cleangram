from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from ...utils import Presets
from ..types import (ForceReply, InlineKeyboardMarkup, Message,
                     ReplyKeyboardMarkup, ReplyKeyboardRemove, Response)
from .base import TelegramMethod


@dataclass
class SendDice(TelegramMethod, response=Response[Message]):
    """
    Use this method to send an animated emoji that will display
    a random value. On success, the sent Message is returned.

    Reference: https://core.telegram.org/bots/api#senddice
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    emoji: Optional[str] = field(default=None)
    """Emoji on which the dice throw animation is based. Currently,
    must be one of “”, “”, “”, “”, “”, or “”. Dice can have
    values 1-6 for “”, “” and “”, values 1-5 for “” and “”, and
    values 1-64 for “”. Defaults to “”"""

    disable_notification: Optional[bool] = field(default=None)
    """Sends the message silently. Users will receive a
    notification with no sound."""

    protect_content: Optional[bool] = field(default=None)
    """Protects the contents of the sent message from forwarding"""

    reply_to_message_id: Optional[int] = field(default=None)
    """If the message is a reply, ID of the original message"""

    allow_sending_without_reply: Optional[bool] = field(default=None)
    """Pass True, if the message should be sent even if the
    specified replied-to message is not found"""

    reply_markup: Optional[
        Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ]
    ] = field(default=None)
    """Additional interface options. A JSON-serialized object for
    an inline keyboard, custom reply keyboard, instructions to
    remove reply keyboard or to force a reply from the user."""

    def preset(self, presets: Presets):
        presets.disable_notification(self)
        presets.protect_content(self)
        presets.allow_sending_without_reply(self)
        return super(SendDice, self).preset(presets)
