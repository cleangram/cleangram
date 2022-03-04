from __future__ import annotations

from dataclasses import dataclass

from ..types import Response, WebhookInfo
from .base import TelegramMethod


@dataclass
class GetWebhookInfo(TelegramMethod, response=Response[WebhookInfo]):
    """
    Use this method to get current webhook status. Requires no
    parameters. On success, returns a WebhookInfo object. If the
    bot is using getUpdates, will return an object with the url
    field empty.

    Reference: https://core.telegram.org/bots/api#getwebhookinfo
    """
