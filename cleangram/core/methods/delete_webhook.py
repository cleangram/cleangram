from dataclasses import dataclass
from typing import Optional

from .base import TelegramMethod
from ..types import Response


@dataclass
class DeleteWebhook(TelegramMethod, response=Response[bool]):
    drop_pending_updates: Optional[bool] = None
