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


class SendPoll(TelegramPath, abc.ABC, response=Response[Message]):
    """
    Use this method to send a native poll. On success, the sent Message is
    returned.

    Reference: https://core.telegram.org/bots/api#sendpoll
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    channel (in the format @channelusername)"""

    question: str
    """Poll question, 1-300 characters"""

    options: List[str]
    """A JSON-serialized list of answer options, 2-10 strings 1-100
    characters each"""

    is_anonymous: Optional[bool] = None
    """True, if the poll needs to be anonymous, defaults to True"""

    type: Optional[str] = None
    """Poll type, “quiz” or “regular”, defaults to “regular”"""

    allows_multiple_answers: Optional[bool] = None
    """True, if the poll allows multiple answers, ignored for polls in quiz
    mode, defaults to False"""

    correct_option_id: Optional[int] = None
    """0-based identifier of the correct answer option, required for polls in
    quiz mode"""

    explanation: Optional[str] = None
    """Text that is shown when a user chooses an incorrect answer or taps on
    the lamp icon in a quiz-style poll, 0-200 characters with at most 2
    line feeds after entities parsing"""

    explanation_parse_mode: Optional[str] = None
    """Mode for parsing entities in the explanation. See formatting options
    for more details."""

    explanation_entities: Optional[List[MessageEntity]] = None
    """A JSON-serialized list of special entities that appear in the poll
    explanation, which can be specified instead of parse_mode"""

    open_period: Optional[int] = None
    """Amount of time in seconds the poll will be active after creation,
    5-600. Can't be used together with close_date."""

    close_date: Optional[int] = None
    """Point in time (Unix timestamp) when the poll will be automatically
    closed. Must be at least 5 and no more than 600 seconds in the future.
    Can't be used together with open_period."""

    is_closed: Optional[bool] = None
    """Pass True, if the poll needs to be immediately closed. This can be
    useful for poll preview."""

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
