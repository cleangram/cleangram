import contextlib
import json

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
        :param bot:
        :param path:
        :param timeout:
        :return:
        """
        with contextlib.ExitStack() as stack:
            data = {n: json.dumps(o) if isinstance(o, (list, dict)) else o for n, o in path.get_data().items()}
            print(data)
            return self.check(
                http_resp=await self._client.post(
                    url=bot.base_url(path),
                    files={n: stack.enter_context(f.open())
                           for n, f in path.get_files().items()},
                    data=data,
                    timeout=(timeout or 1)+.1,
                ),
                path=path
            ).result

    async def close(self):
        await self._client.aclose()
