import abc

from dataclass_factory import Factory, Schema
from httpx import AsyncClient
import json

from cleangram.methods import TelegramMethod
from cleangram.types import Response
from cleangram.env import env


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
        self.parse_mode = parse_mode

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self.__http.__aexit__(exc_type, exc_val, exc_tb)

    async def __call__(self, call: TelegramMethod, timeout: int = 10):
        return (await self._request(call, timeout)).result

    async def _request(self, call: TelegramMethod, timeout: int) -> Response:
        call.preset(self)
        data = self.__factory.dump(call)
        response = await self.__http.post(
            url=self._base_url(call),
            data=data,
            timeout=timeout + .1
        )
        return self.__factory.load(
            data=json.loads(response.content),
            class_=call.response
        )

    def _base_url(self, call: TelegramMethod) -> str:
        return f"{self.__endpoint}/bot{self.__token}/{call.path}"

    async def cleanup(self):
        await self.__http.aclose()
