from contextlib import ExitStack

import abc
from typing import TypeVar, cast

from dataclass_factory import Factory, Schema

from ..exceptions import check
from ..env import env
from ..http.httpx_ import HttpX
from ..methods import TelegramMethod
from ..utils import Presets

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
        self.__presets = Presets(
            _parse_mode=parse_mode,
            _disable_web_page_preview=disable_web_page_preview,
            _protect_content=protect_content,
            _allow_sending_without_reply=allow_sending_without_reply,
            _disable_notification=disable_notification,
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self.__http.__aexit__(exc_type, exc_val, exc_tb)

    async def cleanup(self):
        await self.__http.close()

    async def __call__(self, call: TelegramMethod, timeout: int = 10) -> T:
        url = self._base_url(call)
        files = call.preset(self.__presets)
        data = self.__factory.dump(call)
        with ExitStack() as stack:
            files = {n: stack.enter_context(f) for n, f in files.items()}
            raw = await self.__http(url, data, files, timeout)
        response = self.__factory.load(raw, call.__response__)
        check(response)
        return cast(T, response)

    def _base_url(self, call: TelegramMethod) -> str:
        return f"{self.__endpoint}/bot{self.__token}/{call.__class__.__name__}"
