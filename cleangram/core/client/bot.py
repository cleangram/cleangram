from typing import List, Union

from .base import BaseBot
from ..types import User, Update, Message, InputFile, WebhookInfo
from ..methods import GetMe, GetUpdates, SendMessage, SetWebhook, GetWebhookInfo


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

    async def set_webhook(
        self,
        url: str,
        certificate: InputFile = None,
        ip_address: str = None,
        max_connections: int = None,
        allowed_updates: List[str] = None,
        drop_pending_updates: bool = None
    ) -> bool:
        return await self(SetWebhook(
            url=url,
            certificate=certificate,
            ip_address=ip_address,
            max_connections=max_connections,
            allowed_updates=allowed_updates,
            drop_pending_updates=drop_pending_updates
        ))

    async def get_webhook_info(self) -> WebhookInfo:
        return await self(GetWebhookInfo())

    async def send_message(
        self,
        chat_id: Union[int, str],
        text: str
    ) -> Message:
        return await self(SendMessage(
            chat_id=chat_id,
            text=text
        ))
