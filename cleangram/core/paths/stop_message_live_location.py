import abc
from typing import Optional, Union

from ...core.objects.response import Response
from ..bot.bot import Bot
from ..objects import InlineKeyboardMarkup, Message, TelegramObject
from .base import TelegramPath


class StopMessageLiveLocation(
    TelegramPath, abc.ABC, response=Response[Union[bool, Message]]
):
    """
    Use this method to stop updating a live location message before
    live_period expires. On success, if the message is not an inline
    message, the edited Message is returned, otherwise True is returned.

    Reference: https://core.telegram.org/bots/api#stopmessagelivelocation
    """

    chat_id: Union[int, None, str] = None
    """Required if inline_message_id is not specified. Unique identifier for
    the target chat or username of the target channel (in the format
    @channelusername)"""

    message_id: Optional[int] = None
    """Required if inline_message_id is not specified. Identifier of the
    message with live location to stop"""

    inline_message_id: Optional[str] = None
    """Required if chat_id and message_id are not specified. Identifier of
    the inline message"""

    reply_markup: Optional[InlineKeyboardMarkup] = None
    """A JSON-serialized object for a new inline keyboard."""

    def adjust(self, bot: Bot, result: Union[bool, Message]):
        if isinstance(result, TelegramObject):
            result.adjust(bot)
