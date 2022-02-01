from __future__ import annotations

from dataclasses import dataclass
from typing import Type, ClassVar, TYPE_CHECKING, Dict, Any

from cleangram.types import Response, InputFile

if TYPE_CHECKING:
    from cleangram.client import BaseBot


@dataclass
class TelegramMethod:
    response: ClassVar[Type[Response]]
    path: ClassVar[str]
    defaults: ClassVar[Dict[str, Any]]

    def __init_subclass__(cls, /, **kwargs):
        cls.response = kwargs.get("response")
        cls.path = cls.__name__

    def __post_init__(self):
        self.__files__: Dict[str, InputFile] = {}

    def preset(self, bot: BaseBot):
        pass
