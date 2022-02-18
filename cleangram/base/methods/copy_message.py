from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Union

from ..types import (
    ForceReply,
    InlineKeyboardMarkup,
    MessageEntity,
    MessageId,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Response,
)
from .base import TelegramMethod

from ...utils import Presets


@dataclass
class CopyMessage(TelegramMethod, response=Response[MessageId]):
    """
    Use this method to copy messages of any kind. Service
    messages and invoice messages can't be copied. The method is
    analogous to the method forwardMessage, but the copied
    message doesn't have a link to the original message. Returns
    the MessageId of the sent message on success.

    Reference: https://core.telegram.org/bots/api#copymessage
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    from_chat_id: Union[str, int]
    """Unique identifier for the chat where the original message
    was sent (or channel username in the format
    @channelusername)"""

    message_id: int
    """Message identifier in the chat specified in from_chat_id"""

    caption: Optional[str] = field(default=None)
    """New caption for media, 0-1024 characters after entities
    parsing. If not specified, the original caption is kept"""

    parse_mode: Optional[str] = field(default=None)
    """Mode for parsing entities in the new caption. See formatting
    options for more details."""

    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """A JSON-serialized list of special entities that appear in
    the new caption, which can be specified instead of
    parse_mode"""

    disable_notification: Optional[bool] = field(default=None)
    """Sends the message silently. Users will receive a
    notification with no sound."""

    protect_content: Optional[bool] = field(default=None)
    """Protects the contents of the sent message from forwarding
    and saving"""

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
        presets.parse_mode(self)
        presets.disable_notification(self)
        presets.protect_content(self)
        presets.allow_sending_without_reply(self)
        return super(CopyMessage, self).preset(presets)
