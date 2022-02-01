from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from cleangram.types import (
    Response,
    UserProfilePhotos
)
from .base import TelegramMethod


@dataclass
class GetUserProfilePhotos(TelegramMethod, response=Response[UserProfilePhotos]):
    """
    Use this method to get a list of profile pictures for a
    user. Returns a UserProfilePhotos object.

    Reference: https://core.telegram.org/bots/api#getuserprofilephotos
    """

    user_id: int
    """Unique identifier of the target user"""

    offset: Optional[int] = field(default=None)
    """Sequential number of the first photo to be returned. By
    default, all photos are returned."""

    limit: Optional[int] = field(default=None)
    """Limits the number of photos to be retrieved. Values between
    1-100 are accepted. Defaults to 100."""
