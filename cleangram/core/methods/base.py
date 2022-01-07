from typing import Type

from ..types import Response


class TelegramMethod:
    response: Type[Response]
    path: str

    def __init_subclass__(cls, /, **kwargs):
        cls.response = kwargs.get("response")
        cls.path = cls.__name__
