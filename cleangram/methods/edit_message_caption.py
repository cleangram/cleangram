from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Union

from ..types import InlineKeyboardMarkup, Message, MessageEntity, Response
from .base import TelegramMethod

from ..utils import Presets


@dataclass
class EditMessageCaption(TelegramMethod, response=Response[Union[Message, bool]]):
    """
    Use this method to edit captions of messages. On success, if
    the edited message is not an inline message, the edited
    Message is returned, otherwise True is returned.

    Reference: https://core.telegram.org/bots/api#editmessagecaption
    """

    chat_id: Optional[Union[str, int]] = field(default=None)
    """Required if inline_message_id is not specified. Unique
    identifier for the target chat or username of the target
    channel (in the format @channelusername)"""

    message_id: Optional[int] = field(default=None)
    """Required if inline_message_id is not specified. Identifier
    of the message to edit"""

    inline_message_id: Optional[str] = field(default=None)
    """Required if chat_id and message_id are not specified.
    Identifier of the inline message"""

    caption: Optional[str] = field(default=None)
    """New caption of the message, 0-1024 characters after entities
    parsing"""

    parse_mode: Optional[str] = field(default=None)
    """Mode for parsing entities in the message caption. See
    formatting options for more details."""

    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """A JSON-serialized list of special entities that appear in
    the caption, which can be specified instead of parse_mode"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """A JSON-serialized object for an inline keyboard."""

    def preset(self, presets: Presets):
        presets.parse_mode(self)
        return super(EditMessageCaption, self).preset(presets)
