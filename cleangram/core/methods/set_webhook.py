from dataclasses import dataclass, field
from typing import Optional, List

from .base import TelegramMethod
from ..types import Response, InputFile


@dataclass
class SetWebhook(TelegramMethod, response=Response[bool]):
    url: str
    certificate: Optional[InputFile] = None
    ip_address: Optional[str] = None
    max_connections: Optional[int] = None
    allowed_updates: Optional[List[str]] = field(default_factory=list)
    drop_pending_updates: Optional[bool] = None
