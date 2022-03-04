from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Union

from ...utils import Presets
from ..types import InlineKeyboardMarkup, Message, MessageEntity, Response
from .base import TelegramMethod


@dataclass
class EditMessageText(TelegramMethod, response=Response[Union[Message, bool]]):
    """
    Use this method to edit text and game messages. On success,
    if the edited message is not an inline message, the edited
    Message is returned, otherwise True is returned.

    Reference: https://core.telegram.org/bots/api#editmessagetext
    """

    text: str
    """New text of the message, 1-4096 characters after entities
    parsing"""

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

    parse_mode: Optional[str] = field(default=None)
    """Mode for parsing entities in the message text. See
    formatting options for more details."""

    entities: Optional[List[MessageEntity]] = field(default=None)
    """A JSON-serialized list of special entities that appear in
    message text, which can be specified instead of parse_mode"""

    disable_web_page_preview: Optional[bool] = field(default=None)
    """Disables link previews for links in this message"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """A JSON-serialized object for an inline keyboard."""

    def preset(self, presets: Presets):
        presets.parse_mode(self)
        presets.disable_web_page_preview(self)
        return super(EditMessageText, self).preset(presets)
