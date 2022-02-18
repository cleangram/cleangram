from abc import ABC

import abc

from typing import Dict

import contextlib

from ...base.http.request import Request


class AioHttp(contextlib.AbstractAsyncContextManager, ABC):
    @abc.abstractmethod
    async def json(self, request: Request) -> Dict:
        ...

    @abc.abstractmethod
    async def close(self):
        ...
