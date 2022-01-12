from dataclasses import dataclass
from typing import Optional, List

from .base import TelegramMethod
from ..types import (
    Response,
    Update
)


@dataclass
class GetUpdates(TelegramMethod, response=Response[List[Update]]):
    """
        Reference: https://core.telegram.org/bots/api#getupdates
    """
    offset: Optional[int] = None
    limit: Optional[int] = None
    timeout: Optional[int] = None
    allowed_updates: Optional[List[str]] = None
