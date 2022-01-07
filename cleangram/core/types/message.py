from dataclasses import dataclass
from typing import Optional

from .chat import Chat


@dataclass
class Message:
    """
    Reference: https://core.telegram.org/bots/api#message
    """
    message_id: int
    date: int
    chat: Chat
    text: Optional[str] = None
