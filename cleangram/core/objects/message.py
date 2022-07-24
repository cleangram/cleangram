from typing import Optional

from .base import TelegramObject
from .chat import Chat


class Message(TelegramObject):
    message_id: int
    date: int
    chat: Chat
    text: Optional[str] = None
