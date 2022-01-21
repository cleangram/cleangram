import os
from typing import List

from .router import Router
from .workers import Polling
from ..env import env


class App(Router):
    def __init__(
        self,
        tokens: List[str] = env.TELEGRAM_BOT_TOKEN.split(),
        webhook_endpoint: str = env.WEBHOOK_ENDPOINT,
        telegram_endpoint: str = env.TELEGRAM_API_ENDPOINT,
        **router_kwargs
    ) -> None:
        self.tokens = tokens
        super(App, self).__init__(**router_kwargs)

    @property
    def polling(self):
        return Polling(self)
