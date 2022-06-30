from typing import Optional

from ...core.objects.response import Response
from .base import TelegramPath


class DeleteWebhook(TelegramPath, response=Response[bool]):
    """
    Use this method to remove webhook integration if you decide to switch
    back to getUpdates. Returns True on success.

    Reference: https://core.telegram.org/bots/api#deletewebhook
    """

    drop_pending_updates: Optional[bool] = None
    """Pass True to drop all pending updates"""
