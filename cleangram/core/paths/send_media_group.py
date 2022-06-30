import abc
from typing import List, Optional, Union

from ...core.objects.response import Response
from ..bot.bot import Bot
from ..objects import InputMedia, Message
from .base import TelegramPath


class SendMediaGroup(TelegramPath, abc.ABC, response=Response[List[Message]]):
    """
    Use this method to send a group of photos, videos, documents or audios
    as an album. Documents and audio files can be only grouped in an album
    with messages of the same type. On success, an array of Messages that
    were sent is returned.

    Reference: https://core.telegram.org/bots/api#sendmediagroup
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    channel (in the format @channelusername)"""

    media: List[InputMedia]
    """A JSON-serialized array describing messages to be sent, must include
    2-10 items"""

    disable_notification: Optional[bool] = None
    """Sends messages silently. Users will receive a notification with no
    sound."""

    protect_content: Optional[bool] = None
    """Protects the contents of the sent messages from forwarding and saving"""

    reply_to_message_id: Optional[int] = None
    """If the messages are a reply, ID of the original message"""

    allow_sending_without_reply: Optional[bool] = None
    """Pass True, if the message should be sent even if the specified
    replied-to message is not found"""

    def adjust(self, bot: Bot, result: List[Message]):
        for r in result:
            r.adjust(bot)

    def prepare(self, bot: Bot):
        for m in self.media:
            m.parse_mode = bot.config.preset.parse_mode(m.parse_mode)
            m.media = self.attach(m.media)
            if hasattr(m.media, 'thumb'):
                m.thumb = self.attach(m.thumb)
