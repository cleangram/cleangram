import abc

from dataclass_factory import Factory, Schema
from httpx import AsyncClient
import json

from cleangram.core.methods import TelegramMethod
from ..types import Response
from ..utils import ParseMode, Presets
from ...env import env


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
        self.__http = AsyncClient()
        self.__factory = Factory(default_schema=Schema(omit_default=True))
        self.__presets = Presets(
            parse_mode=parse_mode,
            disable_web_page_preview=disable_web_page_preview
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self.__http.__aexit__(exc_type, exc_val, exc_tb)

    async def __call__(self, call: TelegramMethod, timeout: int = 10):
        return (await self._request(call, timeout)).result

    async def _request(self, call: TelegramMethod, timeout: int) -> Response:
        response = await self.__http.post(
            url=self._base_url(call),
            data=self.__factory.dump(call),
            timeout=timeout + .1
        )
        return self.__factory.load(json.loads(response.content), call.response)

    def _base_url(self, call: TelegramMethod) -> str:
        return f"{self.__endpoint}/bot{self.__token}/{call.path}"

    async def cleanup(self):
        await self.__http.aclose()
