import abc
import contextlib


class Http(contextlib.AbstractAsyncContextManager):
    @abc.abstractmethod
    async def __call__(self, url: str, data: dict, files: dict, timeout: float):
        ...
