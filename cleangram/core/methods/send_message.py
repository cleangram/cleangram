from dataclasses import dataclass
from typing import Union

from .base import TelegramMethod
from ..types import Message, Response


@dataclass
class SendMessage(TelegramMethod, response=Response[Message]):
    chat_id: Union[int, str]
    text: str
