from typing import List, Optional, Union

from ...core.objects.response import Response
from ..bot.bot import Bot
from ..objects import (
    ForceReply,
    InlineKeyboardMarkup,
    MessageEntity,
    MessageId,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from .base import TelegramPath


class CopyMessage(TelegramPath, response=Response[MessageId]):
    """
    Use this method to copy messages of any kind. Service messages and
    invoice messages can't be copied. The method is analogous to the
    method forwardMessage, but the copied message doesn't have a link to
    the original message. Returns the MessageId of the sent message on
    success.

    Reference: https://core.telegram.org/bots/api#copymessage
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    channel (in the format @channelusername)"""

    from_chat_id: Union[int, str]
    """Unique identifier for the chat where the original message was sent (or
    channel username in the format @channelusername)"""

    message_id: int
    """Message identifier in the chat specified in from_chat_id"""

    caption: Optional[str] = None
    """New caption for media, 0-1024 characters after entities parsing. If
    not specified, the original caption is kept"""

    parse_mode: Optional[str] = None
    """Mode for parsing entities in the new caption. See formatting options
    for more details."""

    caption_entities: Optional[List[MessageEntity]] = None
    """A JSON-serialized list of special entities that appear in the new
    caption, which can be specified instead of parse_mode"""

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

    def prepare(self, bot: Bot):
        self.parse_mode = bot.config.preset.parse_mode(self.parse_mode)
