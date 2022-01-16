from dataclasses import dataclass

from .base import TelegramMethod
from ..types import Response, WebhookInfo


@dataclass
class GetWebhookInfo(TelegramMethod, response=Response[WebhookInfo]):
    ...
