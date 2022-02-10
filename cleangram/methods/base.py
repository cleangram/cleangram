from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Dict, Type

from ..types import InputFile, Response

from ..utils import Presets


@dataclass
class TelegramMethod:
    __response__: ClassVar[Type[Response]]

    def __init_subclass__(cls, /, **kwargs):
        cls.__response__ = kwargs.get("response")

    def preset(self, presets: Presets) -> Dict[str, InputFile]:
        files: Dict[str, InputFile] = {}
        return files
