import os
from typing import List

from starlette.applications import Starlette

from .router import Router
from .workers import Polling
from ..env import env


class App(Router):
    def __init__(
        self,
        token: str = env.TELEGRAM_BOT_TOKEN,
        webhook_endpoint: str = env.WEBHOOK_ENDPOINT,
        telegram_endpoint: str = env.TELEGRAM_API_ENDPOINT,
        **router_kwargs
    ) -> None:
        self.token = token
        super(App, self).__init__(**router_kwargs)

    @property
    def polling(self):
        return Polling(self)

    @property
    def st(self) -> Starlette:
        st = Starlette()

        return st
