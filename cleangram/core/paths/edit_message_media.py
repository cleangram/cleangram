import abc
from typing import Optional, Union

from ...core.objects.response import Response
from ..bot.bot import Bot
from ..objects import InlineKeyboardMarkup, InputMedia, Message, TelegramObject
from .base import TelegramPath


class EditMessageMedia(
    TelegramPath, abc.ABC, response=Response[Union[bool, Message]]
):
    """
    Use this method to edit animation, audio, document, photo, or video
    messages. If a message is part of a message album, then it can be
    edited only to an audio for audio albums, only to a document for
    document albums and to a photo or a video otherwise. When an inline
    message is edited, a new file can't be uploaded; use a previously
    uploaded file via its file_id or specify a URL. On success, if the
    edited message is not an inline message, the edited Message is
    returned, otherwise True is returned.

    Reference: https://core.telegram.org/bots/api#editmessagemedia
    """

    media: InputMedia
    """A JSON-serialized object for a new media content of the message"""

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

    reply_markup: Optional[InlineKeyboardMarkup] = None
    """A JSON-serialized object for a new inline keyboard."""

    def adjust(self, bot: Bot, result: Union[bool, Message]):
        if isinstance(result, TelegramObject):
            result.adjust(bot)
