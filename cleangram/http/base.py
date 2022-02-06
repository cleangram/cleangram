import contextlib

import abc


class Http(contextlib.AbstractAsyncContextManager):
    @abc.abstractmethod
    async def post(self, url: str, data: dict, files: dict, timeout: float):
        ...
