from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .input_message_content import InputMessageContent


@dataclass
class InputLocationMessageContent(InputMessageContent):
    """
    Represents the content of a location message to be sent as
    the result of an inline query.
    Reference: https://core.telegram.org/bots/api#inputlocationmessagecontent
    """

    latitude: float
    """Latitude of the location in degrees"""

    longitude: float
    """Longitude of the location in degrees"""

    horizontal_accuracy: Optional[float] = field(default=None)
    """Optional. The radius of uncertainty for the location,
    measured in meters; 0-1500"""

    live_period: Optional[int] = field(default=None)
    """Optional. Period in seconds for which the location can be
    updated, should be between 60 and 86400."""

    heading: Optional[int] = field(default=None)
    """Optional. For live locations, a direction in which the user
    is moving, in degrees. Must be between 1 and 360 if
    specified."""

    proximity_alert_radius: Optional[int] = field(default=None)
    """Optional. For live locations, a maximum distance for
    proximity alerts about approaching another chat member, in
    meters. Must be between 1 and 100000 if specified."""
