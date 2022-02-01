from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .base import TelegramType
from .photo_size import PhotoSize


@dataclass
class UserProfilePhotos(TelegramType):
    """
    This object represent a user's profile pictures.
    Reference: https://core.telegram.org/bots/api#userprofilephotos
    """

    total_count: int
    """Total number of profile pictures the target user has"""

    photos: List[List[PhotoSize]]
    """Requested profile pictures (in up to 4 sizes each)"""
