import abc
from typing import Optional, Union

from ...core.objects.response import Response
from ..bot.bot import Bot
from ..objects import (
    ForceReply,
    InlineKeyboardMarkup,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from .base import TelegramPath


class SendContact(TelegramPath, abc.ABC, response=Response[Message]):
    """
    Use this method to send phone contacts. On success, the sent Message
    is returned.

    Reference: https://core.telegram.org/bots/api#sendcontact
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    channel (in the format @channelusername)"""

    phone_number: str
    """Contact's phone number"""

    first_name: str
    """Contact's first name"""

    last_name: Optional[str] = None
    """Contact's last name"""

    vcard: Optional[str] = None
    """Additional data about the contact in the form of a vCard, 0-2048 bytes"""

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
    keyboard, custom reply keyboard, instructions to remove keyboard or to
    force a reply from the user."""

    def adjust(self, bot: Bot, result: Message):
        result.adjust(bot)
