import contextlib
import abc

from typing import TypeVar

from dataclass_factory import Factory, Schema
import json

from cleangram.http.httpx_ import HttpX
from cleangram.methods import TelegramMethod
from cleangram.types import Response
from cleangram.env import env

T = TypeVar("T")


class BaseBot(abc.ABC):
    def __init__(
        self,
        token: str,
        endpoint: str = env.TELEGRAM_API_ENDPOINT,
        parse_mode: str = None,
        disable_web_page_preview: bool = None
    ) -> None:
        self.__token = token
        self.__endpoint = endpoint
        self.__http = HttpX()
        self.__factory = Factory(default_schema=Schema(omit_default=True))
        self.parse_mode = parse_mode

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self.__http.__aexit__(exc_type, exc_val, exc_tb)

    async def cleanup(self):
        await self.__http.close()

    async def __call__(self, call: TelegramMethod, timeout: int = 10) -> T:
        files = call.preset(self) or {}
        data = self.__factory.dump(call)
        data = {k: json.dumps(v) if isinstance(v, (dict, list)) else v for k, v in data.items()}
        url = self._base_url(call)
        with contextlib.ExitStack() as stack:
            files = {n: stack.enter_context(f) for n, f in files.items()}
            http_resp = await self.__http.post(url, data, files, timeout)
        return (self.__factory.load(json.loads(http_resp), call.__response__)).result

    def _base_url(self, call: TelegramMethod) -> str:
        return f"{self.__endpoint}/bot{self.__token}/{call.__class__.__name__}"
