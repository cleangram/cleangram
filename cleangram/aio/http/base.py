import abc
import contextlib
from abc import ABC
from typing import Dict

from ...base.http.base import BaseHttp
from ...base.http.request import Request


class AioHttp(BaseHttp, contextlib.AbstractAsyncContextManager, ABC):
    @abc.abstractmethod
    async def json(self, request: Request) -> Dict:
        ...

    @abc.abstractmethod
    async def close(self):
        ...
