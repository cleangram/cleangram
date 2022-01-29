from __future__ import annotations

from dataclasses import dataclass
from typing import Type, ClassVar, TYPE_CHECKING

from ..types import Response

if TYPE_CHECKING:
    from ..client.bot import Bot


@dataclass
class TelegramMethod:
    response: ClassVar[Type[Response]]
    path: ClassVar[str]

    def __init_subclass__(cls, /, **kwargs):
        cls.response = kwargs.get("response")
        cls.path = cls.__name__

    def preset(self, bot: Bot):
        pass
