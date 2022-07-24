from .base import TelegramObject


class Chat(TelegramObject):
    id: int
    type: str
