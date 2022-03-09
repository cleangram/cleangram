from typing import Type, TypeVar, cast

from ...base.client.bot import BaseBot
from ...base.methods.base import TelegramMethod
from ..http.base import AioHttp
from ..http.httpx_ import HttpX

T = TypeVar("T")


class AioBaseBot(BaseBot):
    __http__: Type[AioHttp] = HttpX

    async def __call__(self, call: TelegramMethod, timeout: float = None) -> T:
        return cast(T, self._build_result(
            await self.http.json(self._build_request(call, timeout)), call
        ))

    async def __aenter__(self):
        await self.http.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self.http.__aexit__(exc_type, exc_val, exc_tb)

    async def cleanup(self):
        await self.http.close()
