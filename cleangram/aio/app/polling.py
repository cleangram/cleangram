from __future__ import annotations

import asyncio
import contextlib
from typing import TYPE_CHECKING

from ..client.bot import Bot
from ..methods import TelegramMethod
from ...base import Update
from ...base.app.worker import BaseWorker

if TYPE_CHECKING:
    from .app import App


class Polling(BaseWorker):
    def __init__(self, app: App) -> None:
        self.__running: bool = False
        self.__app: App = app
        self.__log = app.log.getChild("polling")
        self.__bots = []

    def __bool__(self):
        return self.__running

    async def start(self, *tokens: str):
        self.__running = True
        await self.__app.run_setup()
        await self.__app.run_startup()
        try:
            async with contextlib.AsyncExitStack() as stack:
                stack: contextlib.AsyncExitStack
                self.__bots = [
                    await stack.enter_async_context(Bot(token))
                    for token in tokens
                ]
                await asyncio.gather(*list(map(self._listen_updates, self.__bots)))
        finally:
            await self.__app.run_shutdown()
            await self.__app.run_destroy()

    async def notify(self, update: Update, bot: Bot):
        if processed := await self.__app.notify(update, bot):
            if isinstance(processed, TelegramMethod):
                await bot(processed)

    async def _listen_updates(self, bot: Bot):
        offset = 0
        while self.__running:
            if updates := await bot.get_updates(offset=offset, timeout=30):
                offset = max([u.update_id for u in updates]) + 1
                await asyncio.gather(*[self.notify(u, bot) for u in updates])

    def run(self, *tokens: str):
        try:
            self.__log.info("Starting")
            asyncio.run(self.start(*tokens))
        except (KeyboardInterrupt, SystemExit):
            pass
        finally:
            self.__log.info("Shutdown")
