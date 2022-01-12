from dataclasses import dataclass
from typing import Union, Optional, List

from .base import TelegramMethod
from ..types import (
    Message,
    Response
)


@dataclass
class SendMessage(TelegramMethod, response=Response[Message]):
    """
        Reference: https://core.telegram.org/bots/api#sendmessage
    """
    chat_id: Union[str, int]
    text: str
    parse_mode: Optional[str] = None
    disable_web_page_preview: Optional[bool] = None
    disable_notification: Optional[bool] = None
    protect_content: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    allow_sending_without_reply: Optional[bool] = None
