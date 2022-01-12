from typing import Type

from ..types import Response
from ..utils import Presets


class TelegramMethod:
    response: Type[Response]
    path: str

    def __init_subclass__(cls, /, **kwargs):
        cls.response = kwargs.get("response")
        cls.path = cls.__name__

    def install_presets(self, presets: Presets):
        pass
