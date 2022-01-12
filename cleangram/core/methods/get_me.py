from dataclasses import dataclass

from .base import TelegramMethod
from ..types import (
    User,
    Response
)


@dataclass
class GetMe(TelegramMethod, response=Response[User]):
    """
        Reference: https://core.telegram.org/bots/api#getme
    """
