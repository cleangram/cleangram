from .base import TelegramPath
from ..objects import WebhookInfo, Response


class GetWebhookInfo(TelegramPath[WebhookInfo], response=Response[WebhookInfo]):
    pass
