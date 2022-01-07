from typing import List, Union

from .base import BaseBot
from ..types import User, Update, Message
from ..methods import GetMe, GetUpdates, SendMessage


class Bot(BaseBot):
    async def get_me(self) -> User:
        return await self(GetMe())

    async def get_updates(
        self,
        offset: int = None,
        timeout: int = None
    ) -> List[Update]:
        return await self(GetUpdates(
            offset=offset,
            timeout=timeout
        ), timeout=timeout)

    async def send_message(
        self,
        chat_id: Union[int, str],
        text: str
    ) -> Message:
        return await self(SendMessage(
            chat_id=chat_id,
            text=text
        ))
