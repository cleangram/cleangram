from typing import Optional, Any

from ..http import HttpX
from ...core.bot.base import BaseBot
from ...core.paths.base import TelegramPath
from ...core.paths.get_me import GetMe
from ...core.objects.response import T


class Bot(BaseBot):
    __http__ = HttpX

    async def __aenter__(self):
        await self.update_me()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.cleanup()

    async def __call__(self, path: TelegramPath, http_timeout: Optional[float] = None) -> T:
        return await self.http(self, path, http_timeout)

    async def update_me(self):
        self._me = await self.get_me()

    async def cleanup(self):
        await self.http.close()

    async def get_me(self, http_timeout: Optional[float] = None) -> Any:
        return await self(
            GetMe(),
            http_timeout=http_timeout
        )
