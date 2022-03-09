import abc

from .request import Request


class BaseHttp(abc.ABC):
    @abc.abstractmethod
    def json(self, request: Request): ...

    @abc.abstractmethod
    def close(self): ...
