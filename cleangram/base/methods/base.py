from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Dict, Type

from ..types import InputFile, Response

from ...utils import Presets


@dataclass
class TelegramMethod:
    __response__: ClassVar[Type[Response]]
    __method__: ClassVar[str]

    def __init_subclass__(cls, /, **kwargs):
        cls.__response__ = kwargs.get("response")
        cls.__method__ = f"{cls.__name__[0].lower()}{cls.__name__[1:]}"

    def preset(self, presets: Presets) -> Dict[str, InputFile]:
        files: Dict[str, InputFile] = {}
        return files
