import abc
from typing import Generic, ClassVar, Type, Optional, Dict, Union

from pydantic import PrivateAttr

from ..objects import Component, Response, T, InputFile


class TelegramPath(Component, Generic[T], abc.ABC):
    __response__: ClassVar[Type[Response[T]]]

    _files: Optional[Dict[str, InputFile]] = PrivateAttr(default_factory=dict)

    @property
    def files(self):
        return self._files

    @property
    def data(self):
        return self.dict(exclude_none=True, exclude=self._files.keys())

    def __init_subclass__(cls, /, **kwargs) -> None:
        super().__init_subclass__()
        cls.__response__ = kwargs.get("response")

    def build_response(self, data: dict):
        return self.__response__.parse_obj(data)

    def preset(self, bot):
        ...

    def adjust(self, bot, result: T):
        ...

    def attach(self, file: Union[InputFile, str], name: str = None) -> Optional[str]:
        ...
