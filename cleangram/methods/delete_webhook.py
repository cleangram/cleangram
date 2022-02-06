from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ..types import Response
from .base import TelegramMethod


@dataclass
class DeleteWebhook(TelegramMethod, response=Response[bool]):
    """
    Use this method to remove webhook integration if you decide
    to switch back to getUpdates. Returns True on success.

    Reference: https://core.telegram.org/bots/api#deletewebhook
    """

    drop_pending_updates: Optional[bool] = field(default=None)
    """Pass True to drop all pending updates"""
