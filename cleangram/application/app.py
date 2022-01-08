import asyncio
import logging
import os
from typing import Callable

from ..core import Update, Bot


class Polling:
    def __init__(self, app):
        self.app = app
        self._running = False

    async def start(self):
        self._running = True
        offset = 0
        async with Bot(self.app.tokens[0]) as bot:
            while self._running:
                updates = await bot.get_updates(offset=offset, timeout=3)
                if updates:
                    ids = [u.update_id for u in updates]
                    offset = max(ids)+1
                    await asyncio.gather(*[self.app.notify(update, bot) for update in updates])
                await asyncio.sleep(0.5)

    def run(self):
        try:
            asyncio.run(self.start())
        except (KeyboardInterrupt, SystemExit):
            logging.info("Polling shutdown")


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
