from dataclasses import dataclass, field

from ...base import GetMe
from ...base.client.bot import BaseBot
from ...base.methods.base import TelegramMethod
from ..http.base import AioHttp
from ..http.httpx_ import HttpX


@dataclass
class AioBaseBot(BaseBot):
    http: AioHttp = field(default_factory=HttpX, repr=False)

    async def __call__(self, call: TelegramMethod, timeout: float = None):
        return self._build_result(
            await self.http.json(self._build_request(call, timeout)), call
        )

    async def __aenter__(self):
        await self.http.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self.http.__aexit__(exc_type, exc_val, exc_tb)

    async def cleanup(self):
        await self.http.close()
