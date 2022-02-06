from __future__ import annotations

from dataclasses import dataclass
from typing import Type, ClassVar, TYPE_CHECKING, Dict

from cleangram.types import Response, InputFile

if TYPE_CHECKING:
    from cleangram.client import BaseBot


@dataclass
class TelegramMethod:
    __response__: ClassVar[Type[Response]]

    def __init_subclass__(cls, /, **kwargs):
        cls.__response__ = kwargs.get("response")

    def preset(self, bot: BaseBot) -> Dict[str, InputFile]:
        return {}
