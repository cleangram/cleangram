import abc
from typing import Union

from ...core.objects.response import Response
from ..bot.bot import Bot
from ..objects import Chat
from .base import TelegramPath


class GetChat(TelegramPath, abc.ABC, response=Response[Chat]):
    """
    Use this method to get up to date information about the chat (current
    name of the user for one-on-one conversations, current username of a
    user, group or channel, etc.). Returns a Chat object on success.

    Reference: https://core.telegram.org/bots/api#getchat
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    supergroup or channel (in the format @channelusername)"""

    def adjust(self, bot: Bot, result: Chat):
        result.adjust(bot)
