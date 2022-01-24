from typing import List, Union, Optional

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
        chat_id: Union[str, int],
        text: str,
        parse_mode: Optional[str] = None,
        disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None
    ) -> Message:
        return await self(SendMessage(
            chat_id=chat_id,
            text=text,
            parse_mode=parse_mode,
            disable_web_page_preview=disable_web_page_preview,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply
        ))
