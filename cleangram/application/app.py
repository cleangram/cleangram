import os
from typing import Callable

from .workers import Polling
from ..core import Update, Bot


class App:
    def __init__(self, tokens=None):
        self.messages = []
        self.tokens = tokens or [os.getenv("TELEGRAM_BOT_TOKEN")]

    def message(self, callback: Callable):
        self.messages.append(callback)

    async def notify(self, update: Update, bot: Bot):
        for m in self.messages:
            await m(update.message, bot)

    @property
    def polling(self):
        return Polling(self)
