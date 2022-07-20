import contextlib

import httpx

from cleangram.core import T
from cleangram.core.bot.base import BaseBot
from cleangram.core.http.httpx_ import BaseHttpX
from cleangram.core.paths import TelegramPath


class HttpX(BaseHttpX):
    def __init__(self):
        self._client = httpx.AsyncClient()

    async def __call__(self, bot: BaseBot, path: TelegramPath, timeout: float = 1) -> T:
        """
        make `request`
        call request and get response
        return serialize response and return result
        with self.builder(bot, path, timeout) as (serialize, request):
            return serialize(await self._client.request(request))
        :param bot:
        :param path:
        :param timeout:
        :return:
        """
        path.preset(bot)
        with contextlib.ExitStack() as stack:
            files = {n: stack.enter_context(open(f.path, "rb")) for n, f in path.get_files().items()}
            http_resp = await self._client.post(
                url=bot.base_url(path),
                files=files,
                data=path.get_data(),
                timeout=(timeout or 1)+.1,
            )
        return self.check(http_resp, path).result

    async def close(self):
        await self._client.aclose()
