from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from ..types import (
    InlineKeyboardMarkup,
    Message,
    Response
)
from .base import TelegramMethod


@dataclass
class EditMessageLiveLocation(TelegramMethod, response=Response[Union[Message, bool]]):
    """
    Use this method to edit live location messages. A location
    can be edited until its live_period expires or editing is
    explicitly disabled by a call to stopMessageLiveLocation. On
    success, if the edited message is not an inline message, the
    edited Message is returned, otherwise True is returned.

    Reference: https://core.telegram.org/bots/api#editmessagelivelocation
    """

    latitude: float
    """Latitude of new location"""

    longitude: float
    """Longitude of new location"""

    chat_id: Optional[Union[str, int]] = field(default=None)
    """Required if inline_message_id is not specified. Unique
    identifier for the target chat or username of the target
    channel (in the format @channelusername)"""

    message_id: Optional[int] = field(default=None)
    """Required if inline_message_id is not specified. Identifier
    of the message to edit"""

    inline_message_id: Optional[str] = field(default=None)
    """Required if chat_id and message_id are not specified.
    Identifier of the inline message"""

    horizontal_accuracy: Optional[float] = field(default=None)
    """The radius of uncertainty for the location, measured in
    meters; 0-1500"""

    heading: Optional[int] = field(default=None)
    """Direction in which the user is moving, in degrees. Must be
    between 1 and 360 if specified."""

    proximity_alert_radius: Optional[int] = field(default=None)
    """Maximum distance for proximity alerts about approaching
    another chat member, in meters. Must be between 1 and 100000
    if specified."""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """A JSON-serialized object for a new inline keyboard."""
