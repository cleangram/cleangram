import contextlib

import abc

from ...base.http.base import BaseHttp


class SyncHttp(BaseHttp, contextlib.AbstractContextManager, abc.ABC):
    ...
