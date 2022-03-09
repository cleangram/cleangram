from dataclasses import dataclass, field
from typing import TypeVar, cast, Type

from ...base.client.bot import BaseBot
from ...base.methods import TelegramMethod
from ..http.base import SyncHttp
from ..http.httpx_ import HttpX

T = TypeVar("T")


class SyncBaseBot(BaseBot):
    __http__: Type[SyncHttp] = HttpX

    def __call__(self, call: TelegramMethod, timeout: float = None) -> T:
        return cast(
            T,
            self._build_result(
                self.http.json(self._build_request(call, timeout)), call
            ),
        )

    def __enter__(self):
        self.http.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.http.__exit__(exc_type, exc_val, exc_tb)

    def cleanup(self):
        self.http.close()
