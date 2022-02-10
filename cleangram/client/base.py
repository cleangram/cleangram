import contextlib
import abc

from typing import TypeVar, cast

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
        parse_mode: str = None,
        allow_sending_without_reply: bool = None,
        disable_notification: bool = None,
        disable_web_page_preview: bool = None,
        protect_content: bool = None,
        endpoint: str = env.TELEGRAM_API_ENDPOINT,
    ) -> None:
        self.__token = token
        self.__endpoint = endpoint
        self.__http = HttpX()
        self.__factory = Factory(default_schema=Schema(omit_default=True))
        self.parse_mode = parse_mode
        self.disable_notification = disable_notification
        self.disable_web_page_preview = disable_web_page_preview
        self.protect_content = protect_content
        self.allow_sending_without_reply = allow_sending_without_reply

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self.__http.__aexit__(exc_type, exc_val, exc_tb)

    async def cleanup(self):
        await self.__http.close()

    async def __call__(self, call: TelegramMethod, timeout: int = 10) -> T:
        files = call.preset(self) or {}
        data = self.__factory.dump(call)
        data = {
            k: json.dumps(v) if isinstance(v, (dict, list)) else v
            for k, v in data.items()
        }
        url = self._base_url(call)
        with contextlib.ExitStack() as stack:
            files = {n: stack.enter_context(f) for n, f in files.items()}
            http_resp = await self.__http.post(url, data, files, timeout)
        return cast(
            T, (self.__factory.load(json.loads(http_resp), call.__response__)).result
        )

    def _base_url(self, call: TelegramMethod) -> str:
        return f"{self.__endpoint}/bot{self.__token}/{call.__class__.__name__}"
