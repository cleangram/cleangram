import abc

from dataclass_factory import Factory, Schema
from httpx import AsyncClient
import json

from cleangram.core.methods import TelegramMethod

TG_ENDPOINT = "https://api.telegram.org"


class BaseBot(abc.ABC):
    def __init__(
        self,
        token: str,
        endpoint: str = TG_ENDPOINT
    ) -> None:
        self.__token = token
        self.__endpoint = endpoint
        self.__http = AsyncClient()
        self.__factory = Factory(default_schema=Schema(omit_default=True))

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self.__http.__aexit__(exc_type, exc_val, exc_tb)

    async def __call__(self, method: TelegramMethod, timeout: int = 10):
        response = await self.__http.post(
            url=self._base_url(method),
            data=self.__factory.dump(method),
            timeout=timeout+.1
        )
        return self.__factory.load(json.loads(response.content), method.response).result

    def _base_url(self, method: TelegramMethod) -> str:
        return f"{self.__endpoint}/bot{self.__token}/{method.path}"

    async def cleanup(self):
        await self.__http.aclose()
