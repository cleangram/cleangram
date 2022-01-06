from typing import Type

from ..types import Response, T


class TelegramMethod:
    def __init_subclass__(cls, /, **kwargs):
        cls.response: Type[Response[T]] = kwargs.get("response")
