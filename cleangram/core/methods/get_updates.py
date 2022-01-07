from dataclasses import dataclass
from typing import List, Optional

from ..methods import TelegramMethod
from ..types import Response, Update


@dataclass
class GetUpdates(TelegramMethod, response=Response[List[Update]]):
    offset: Optional[int] = None
    limit: Optional[int] = None
    timeout: Optional[int] = None
    allowed_updates: Optional[List[str]] = None
