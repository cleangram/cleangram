import abc
from typing import Optional

from ...core.objects.response import Response
from ..bot.bot import Bot
from ..objects import InlineKeyboardMarkup, Message
from .base import TelegramPath


class SendGame(TelegramPath, abc.ABC, response=Response[Message]):
    """
    Use this method to send a game. On success, the sent Message is
    returned.

    Reference: https://core.telegram.org/bots/api#sendgame
    """

    chat_id: int
    """Unique identifier for the target chat"""

    game_short_name: str
    """Short name of the game, serves as the unique identifier for the game.
    Set up your games via @BotFather."""

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

    reply_markup: Optional[InlineKeyboardMarkup] = None
    """A JSON-serialized object for an inline keyboard. If empty, one 'Play
    game_title' button will be shown. If not empty, the first button must
    launch the game."""

    def adjust(self, bot: Bot, result: Message):
        result.adjust(bot)
