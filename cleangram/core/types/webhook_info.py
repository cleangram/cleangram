from dataclasses import dataclass
from typing import Optional, List

from .base import TelegramType


@dataclass
class WebhookInfo(TelegramType):
    url: str
    has_custom_certificate: bool
    pending_update_count: int
    ip_address: Optional[str] = None
    last_error_date: Optional[int] = None
    last_error_message: Optional[str] = None
    max_connections: Optional[int] = None
    allowed_updates: Optional[List[str]] = None
