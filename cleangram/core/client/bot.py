from .base import BaseBot
from ..types import User
from ..methods import GetMe


class Bot(BaseBot):
    async def get_me(self) -> User:
        return await self(GetMe())
