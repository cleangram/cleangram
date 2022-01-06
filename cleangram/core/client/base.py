import abc
from dataclasses import dataclass, field

from dataclass_factory import Factory, Schema
from httpx import AsyncClient
import json

from cleangram.core.methods import TelegramMethod


@dataclass
class BaseBot(abc.ABC):
    token: str
    endpoint: str = field(default="https://api.telegram.org")

    async def cleanup(self):
        await self.http.aclose()

    def _base_url(self, method: TelegramMethod) -> str:
        return f"{self.endpoint}/bot{self.token}/{method.__class__.__name__}"

    def __post_init__(self):
        self.http = AsyncClient()
        self.factory = Factory(default_schema=Schema(omit_default=True))

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self.http.__aexit__(exc_type, exc_val, exc_tb)

    async def __call__(self, method: TelegramMethod):
        response = await self.http.post(
            url=self._base_url(method)
        )
        return self.factory.load(json.loads(response.content), method.response)

