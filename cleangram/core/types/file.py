from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .base import TelegramType


@dataclass
class File(TelegramType):
    """
    This object represents a file ready to be downloaded. The
    file can be downloaded via the link
    https://api.telegram.org/file/bot<token>/<file_path>. It is
    guaranteed that the link will be valid for at least 1 hour.
    When the link expires, a new one can be requested by calling
    getFile.
    Reference: https://core.telegram.org/bots/api#file
    """

    file_id: str
    """Identifier for this file, which can be used to download or
    reuse the file"""

    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the
    same over time and for different bots. Can't be used to
    download or reuse the file."""

    file_size: Optional[int] = field(default=None)
    """Optional. File size in bytes, if known"""

    file_path: Optional[str] = field(default=None)
    """Optional. File path. Use
    https://api.telegram.org/file/bot<token>/<file_path> to get
    the file."""
