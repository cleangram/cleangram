import abc
from typing import List, Optional, Union

from ...core.objects.response import Response
from ..bot.bot import Bot
from ..objects import (
    ForceReply,
    InlineKeyboardMarkup,
    Message,
    MessageEntity,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from .base import TelegramPath


class SendMessage(TelegramPath, abc.ABC, response=Response[Message]):
    """
    Use this method to send text messages. On success, the sent Message is
    returned.

    Reference: https://core.telegram.org/bots/api#sendmessage
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    channel (in the format @channelusername)"""

    text: str
    """Text of the message to be sent, 1-4096 characters after entities
    parsing"""

    parse_mode: Optional[str] = None
    """Mode for parsing entities in the message text. See formatting options
    for more details."""

    entities: Optional[List[MessageEntity]] = None
    """A JSON-serialized list of special entities that appear in message
    text, which can be specified instead of parse_mode"""

    disable_web_page_preview: Optional[bool] = None
    """Disables link previews for links in this message"""

    disable_notification: Optional[bool] = None
    """Sends the message silently. Users will receive a notification with no
    sound."""

    protect_content: Optional[bool] = None
    """Protects the contents of the sent message from forwarding and saving"""

    reply_to_message_id: Optional[int] = None
    """If the message is a reply, ID of the original message"""

    allow_sending_without_reply: Optional[bool] = None
    """Pass True, if the message should be sent even if the specified
    replied-to message is not found"""

    reply_markup: Union[
        ForceReply,
        ReplyKeyboardRemove,
        None,
        InlineKeyboardMarkup,
        ReplyKeyboardMarkup,
    ] = None
    """Additional interface options. A JSON-serialized object for an inline
    keyboard, custom reply keyboard, instructions to remove reply keyboard
    or to force a reply from the user."""

    def adjust(self, bot: Bot, result: Message):
        result.adjust(bot)

    def prepare(self, bot: Bot):
        self.parse_mode = bot.config.preset.parse_mode(self.parse_mode)
