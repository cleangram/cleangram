from .base import TelegramMethod
from .get_me import GetMe
from .get_updates import GetUpdates
from .send_message import SendMessage
from .set_webhook import SetWebhook

__all__ = [
    "TelegramMethod",
    "GetMe",
    "GetUpdates",
    "SendMessage",
    "SetWebhook"
]
