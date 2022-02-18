import abc

from typing import Dict

from .request import Request


class BaseHttp(abc.ABC):
    @abc.abstractmethod
    def json(self, request: Request) -> Dict:
        ...

    @abc.abstractmethod
    def close(self):
        ...
