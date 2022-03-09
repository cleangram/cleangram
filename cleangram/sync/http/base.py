import abc
import contextlib
from typing import Dict

from ...base.http.base import BaseHttp
from ...base.http.request import Request


class SyncHttp(BaseHttp, contextlib.AbstractContextManager, abc.ABC):
    @abc.abstractmethod
    def json(self, request: Request) -> Dict: ...

    @abc.abstractmethod
    def close(self) -> None: ...
