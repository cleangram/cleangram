from typing import Union

from .base import TelegramPath
from ..objects import Response, Message


class SendMessage(TelegramPath[Message], response=Response[Message]):
    chat_id: Union[int, str]
    text: str
