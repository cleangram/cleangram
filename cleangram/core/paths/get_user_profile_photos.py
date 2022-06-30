from typing import Optional

from ...core.objects.response import Response
from ..objects import UserProfilePhotos
from .base import TelegramPath


class GetUserProfilePhotos(TelegramPath, response=Response[UserProfilePhotos]):
    """
    Use this method to get a list of profile pictures for a user. Returns
    a UserProfilePhotos object.

    Reference: https://core.telegram.org/bots/api#getuserprofilephotos
    """

    user_id: int
    """Unique identifier of the target user"""

    offset: Optional[int] = None
    """Sequential number of the first photo to be returned. By default, all
    photos are returned."""

    limit: Optional[int] = None
    """Limits the number of photos to be retrieved. Values between 1-100 are
    accepted. Defaults to 100."""
