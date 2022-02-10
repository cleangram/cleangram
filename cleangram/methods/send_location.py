from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from ..types import (
    ForceReply,
    InlineKeyboardMarkup,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Response,
)
from .base import TelegramMethod

from ..utils import Presets


@dataclass
class SendLocation(TelegramMethod, response=Response[Message]):
    """
    Use this method to send point on the map. On success, the
    sent Message is returned.

    Reference: https://core.telegram.org/bots/api#sendlocation
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    latitude: float
    """Latitude of the location"""

    longitude: float
    """Longitude of the location"""

    horizontal_accuracy: Optional[float] = field(default=None)
    """The radius of uncertainty for the location, measured in
    meters; 0-1500"""

    live_period: Optional[int] = field(default=None)
    """Period in seconds for which the location will be updated
    (see Live Locations, should be between 60 and 86400."""

    heading: Optional[int] = field(default=None)
    """For live locations, a direction in which the user is moving,
    in degrees. Must be between 1 and 360 if specified."""

    proximity_alert_radius: Optional[int] = field(default=None)
    """For live locations, a maximum distance for proximity alerts
    about approaching another chat member, in meters. Must be
    between 1 and 100000 if specified."""

    disable_notification: Optional[bool] = field(default=None)
    """Sends the message silently. Users will receive a
    notification with no sound."""

    protect_content: Optional[bool] = field(default=None)
    """Protects the contents of the sent message from forwarding
    and saving"""

    reply_to_message_id: Optional[int] = field(default=None)
    """If the message is a reply, ID of the original message"""

    allow_sending_without_reply: Optional[bool] = field(default=None)
    """Pass True, if the message should be sent even if the
    specified replied-to message is not found"""

    reply_markup: Optional[
        Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ]
    ] = field(default=None)
    """Additional interface options. A JSON-serialized object for
    an inline keyboard, custom reply keyboard, instructions to
    remove reply keyboard or to force a reply from the user."""

    def preset(self, presets: Presets):
        presets.disable_notification(self)
        presets.protect_content(self)
        presets.allow_sending_without_reply(self)
        return super(SendLocation, self).preset(presets)
