from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from ..types import (
    ForceReply,
    InlineKeyboardMarkup,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Response
)
from .base import TelegramMethod


@dataclass
class SendVenue(TelegramMethod, response=Response[Message]):
    """
    Use this method to send information about a venue. On
    success, the sent Message is returned.

    Reference: https://core.telegram.org/bots/api#sendvenue
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    latitude: float
    """Latitude of the venue"""

    longitude: float
    """Longitude of the venue"""

    title: str
    """Name of the venue"""

    address: str
    """Address of the venue"""

    foursquare_id: Optional[str] = field(default=None)
    """Foursquare identifier of the venue"""

    foursquare_type: Optional[str] = field(default=None)
    """Foursquare type of the venue, if known. (For example,
    “arts_entertainment/default”, “arts_entertainment/aquarium”
    or “food/icecream”.)"""

    google_place_id: Optional[str] = field(default=None)
    """Google Places identifier of the venue"""

    google_place_type: Optional[str] = field(default=None)
    """Google Places type of the venue. (See supported types.)"""

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

    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = field(default=None)
    """Additional interface options. A JSON-serialized object for
    an inline keyboard, custom reply keyboard, instructions to
    remove reply keyboard or to force a reply from the user."""
