from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent


@dataclass
class InlineQueryResultVenue(InlineQueryResult):
    """
    Represents a venue. By default, the venue will be sent by
    the user. Alternatively, you can use input_message_content
    to send a message with the specified content instead of the
    venue.
    Reference: https://core.telegram.org/bots/api#inlinequeryresultvenue
    """

    id: str
    """Unique identifier for this result, 1-64 Bytes"""

    latitude: float
    """Latitude of the venue location in degrees"""

    longitude: float
    """Longitude of the venue location in degrees"""

    title: str
    """Title of the venue"""

    address: str
    """Address of the venue"""

    foursquare_id: Optional[str] = field(default=None)
    """Optional. Foursquare identifier of the venue if known"""

    foursquare_type: Optional[str] = field(default=None)
    """Optional. Foursquare type of the venue, if known. (For
    example, “arts_entertainment/default”,
    “arts_entertainment/aquarium” or “food/icecream”.)"""

    google_place_id: Optional[str] = field(default=None)
    """Optional. Google Places identifier of the venue"""

    google_place_type: Optional[str] = field(default=None)
    """Optional. Google Places type of the venue. (See supported
    types.)"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""

    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the
    venue"""

    thumb_url: Optional[str] = field(default=None)
    """Optional. Url of the thumbnail for the result"""

    thumb_width: Optional[int] = field(default=None)
    """Optional. Thumbnail width"""

    thumb_height: Optional[int] = field(default=None)
    """Optional. Thumbnail height"""

    type_: str = field(default="")
    """Type of the result, must be venue"""

    def __post_init__(self):
        self.type_ = "venue"
