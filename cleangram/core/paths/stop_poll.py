from typing import Optional, Union

from ...core.objects.response import Response
from ..objects import InlineKeyboardMarkup, Poll
from .base import TelegramPath


class StopPoll(TelegramPath, response=Response[Poll]):
    """
    Use this method to stop a poll which was sent by the bot. On success,
    the stopped Poll is returned.

    Reference: https://core.telegram.org/bots/api#stoppoll
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    channel (in the format @channelusername)"""

    message_id: int
    """Identifier of the original message with the poll"""

    reply_markup: Optional[InlineKeyboardMarkup] = None
    """A JSON-serialized object for a new message inline keyboard."""
