import abc
from typing import Optional, Union

from ...core.objects.response import Response
from ..bot.bot import Bot
from ..objects import InlineKeyboardMarkup, Message, TelegramObject
from .base import TelegramPath


class EditMessageLiveLocation(
    TelegramPath, abc.ABC, response=Response[Union[bool, Message]]
):
    """
    Use this method to edit live location messages. A location can be
    edited until its live_period expires or editing is explicitly disabled
    by a call to stopMessageLiveLocation. On success, if the edited
    message is not an inline message, the edited Message is returned,
    otherwise True is returned.

    Reference: https://core.telegram.org/bots/api#editmessagelivelocation
    """

    latitude: float
    """Latitude of new location"""

    longitude: float
    """Longitude of new location"""

    chat_id: Union[int, None, str] = None
    """Required if inline_message_id is not specified. Unique identifier for
    the target chat or username of the target channel (in the format
    @channelusername)"""

    message_id: Optional[int] = None
    """Required if inline_message_id is not specified. Identifier of the
    message to edit"""

    inline_message_id: Optional[str] = None
    """Required if chat_id and message_id are not specified. Identifier of
    the inline message"""

    horizontal_accuracy: Optional[float] = None
    """The radius of uncertainty for the location, measured in meters; 0-1500"""

    heading: Optional[int] = None
    """Direction in which the user is moving, in degrees. Must be between 1
    and 360 if specified."""

    proximity_alert_radius: Optional[int] = None
    """The maximum distance for proximity alerts about approaching another
    chat member, in meters. Must be between 1 and 100000 if specified."""

    reply_markup: Optional[InlineKeyboardMarkup] = None
    """A JSON-serialized object for a new inline keyboard."""

    def adjust(self, bot: Bot, result: Union[bool, Message]):
        if isinstance(result, TelegramObject):
            result.adjust(bot)
