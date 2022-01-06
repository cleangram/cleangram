from dataclasses import dataclass, field

from .base import TelegramType


@dataclass
class User(TelegramType):
    id: int
    is_bot: bool
    first_name: str
    username: str
    last_name: str = field(default=None)
