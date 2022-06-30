from ...core.objects.response import Response
from ..objects import WebhookInfo
from .base import TelegramPath


class GetWebhookInfo(TelegramPath, response=Response[WebhookInfo]):
    """
    Use this method to get current webhook status. Requires no parameters.
    On success, returns a WebhookInfo object. If the bot is using
    getUpdates, will return an object with the url field empty.

    Reference: https://core.telegram.org/bots/api#getwebhookinfo
    """
