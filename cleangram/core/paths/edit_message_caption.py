import abc
from typing import List, Optional, Union

from ...core.objects.response import Response
from ..bot.bot import Bot
from ..objects import (
    InlineKeyboardMarkup,
    Message,
    MessageEntity,
    TelegramObject,
)
from .base import TelegramPath


class EditMessageCaption(
    TelegramPath, abc.ABC, response=Response[Union[bool, Message]]
):
    """
    Use this method to edit captions of messages. On success, if the
    edited message is not an inline message, the edited Message is
    returned, otherwise True is returned.

    Reference: https://core.telegram.org/bots/api#editmessagecaption
    """

    chat_id: Union[int, None, str] = None
    """Required if inline_message_id is not specified. Unique identifier for
    the target chat or username of the target channel (in the format
    @channelusername)"""

    message_id: Optional[int] = None
    """Required if inline_message_id is not specified. Identifier of the
    message to edit"""

    inline_message_id: Optional[str] = None
    """Required if chat_id and message_id are not specified. Identifier of
    the inline message"""

    caption: Optional[str] = None
    """New caption of the message, 0-1024 characters after entities parsing"""

    parse_mode: Optional[str] = None
    """Mode for parsing entities in the message caption. See formatting
    options for more details."""

    caption_entities: Optional[List[MessageEntity]] = None
    """A JSON-serialized list of special entities that appear in the caption,
    which can be specified instead of parse_mode"""

    reply_markup: Optional[InlineKeyboardMarkup] = None
    """A JSON-serialized object for an inline keyboard."""

    def adjust(self, bot: Bot, result: Union[bool, Message]):
        if isinstance(result, TelegramObject):
            result.adjust(bot)

    def prepare(self, bot: Bot):
        self.parse_mode = bot.config.preset.parse_mode(self.parse_mode)
