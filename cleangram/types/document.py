from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .base import TelegramType
from .photo_size import PhotoSize


@dataclass
class Document(TelegramType):
    """
    This object represents a general file (as opposed to photos,
    voice messages and audio files).
    Reference: https://core.telegram.org/bots/api#document
    """

    file_id: str
    """Identifier for this file, which can be used to download or
    reuse the file"""

    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the
    same over time and for different bots. Can't be used to
    download or reuse the file."""

    thumb: Optional[PhotoSize] = field(default=None)
    """Optional. Document thumbnail as defined by sender"""

    file_name: Optional[str] = field(default=None)
    """Optional. Original filename as defined by sender"""

    mime_type: Optional[str] = field(default=None)
    """Optional. MIME type of the file as defined by sender"""

    file_size: Optional[int] = field(default=None)
    """Optional. File size in bytes"""
