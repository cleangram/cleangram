from typing import Optional, List

from .base import TelegramPath
from ..objects import InputFile, Response


class SetWebhook(TelegramPath[bool], response=Response[bool]):
    url: str
    certificate: Optional[InputFile] = None
    ip_address: Optional[str] = None
    max_connections: Optional[int] = None
    allowed_updates: Optional[List[str]] = None
    drop_pending_updates: Optional[bool] = None
    secret_token: Optional[str] = None

    def preset(self, bot):
        self.attach(self.certificate, "certificate")
