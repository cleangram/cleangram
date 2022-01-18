import os

from .router import Router
from .workers import Polling


class Cleangram(Router):
    def __init__(
        self,
        tokens=None,
        webhook_endpoint="",
        telegram_endpoint="",
        **router_kwargs
    ) -> None:
        self.tokens = tokens or [os.getenv("TELEGRAM_BOT_TOKEN")]
        super(Cleangram, self).__init__(**router_kwargs)

    @property
    def polling(self):
        return Polling(self)
