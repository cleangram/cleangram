import abc
from typing import Optional, Union

from ...core.objects.response import Response
from ..bot.bot import Bot
from ..objects import Message
from .base import TelegramPath


class ForwardMessage(TelegramPath, abc.ABC, response=Response[Message]):
    """
    Use this method to forward messages of any kind. Service messages
    can't be forwarded. On success, the sent Message is returned.

    Reference: https://core.telegram.org/bots/api#forwardmessage
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    channel (in the format @channelusername)"""

    from_chat_id: Union[int, str]
    """Unique identifier for the chat where the original message was sent (or
    channel username in the format @channelusername)"""

    message_id: int
    """Message identifier in the chat specified in from_chat_id"""

    disable_notification: Optional[bool] = None
    """Sends the message silently. Users will receive a notification with no
    sound."""

    protect_content: Optional[bool] = None
    """Protects the contents of the forwarded message from forwarding and
    saving"""

    def adjust(self, bot: Bot, result: Message):
        result.adjust(bot)
