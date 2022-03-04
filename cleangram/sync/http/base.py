import abc
import contextlib

from ...base.http.base import BaseHttp


class SyncHttp(BaseHttp, contextlib.AbstractContextManager, abc.ABC):
    ...
