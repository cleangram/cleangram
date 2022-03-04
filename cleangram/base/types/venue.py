from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .base import TelegramType
from .location import Location


@dataclass
class Venue(TelegramType):
    """
    This object represents a venue.
    Reference: https://core.telegram.org/bots/api#venue
    """

    location: Location
    """Venue location. Can't be a live location"""

    title: str
    """Name of the venue"""

    address: str
    """Address of the venue"""

    foursquare_id: Optional[str] = field(default=None)
    """Optional. Foursquare identifier of the venue"""

    foursquare_type: Optional[str] = field(default=None)
    """Optional. Foursquare type of the venue. (For example,
    “arts_entertainment/default”, “arts_entertainment/aquarium”
    or “food/icecream”.)"""

    google_place_id: Optional[str] = field(default=None)
    """Optional. Google Places identifier of the venue"""

    google_place_type: Optional[str] = field(default=None)
    """Optional. Google Places type of the venue. (See supported
    types.)"""
