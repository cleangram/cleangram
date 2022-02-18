from __future__ import annotations

from asyncio import Task

from typing import TYPE_CHECKING

import asyncio

from ..client.bot import Bot
from ..methods import TelegramMethod

if TYPE_CHECKING:
    from .app import App


class Polling:
    def __init__(self, app: App) -> None:
        self.__running: bool = False
        self.__app: App = app
        self.__log = app.log.getChild("polling")

    async def start(self, *tokens: str):
        self.__running = True
        await self.__app.emit_startup()
        try:
            await asyncio.gather(*map(self._listen_updates, tokens))
        finally:
            await self.__app.emit_shutdown()

    async def notify(self, update, bot):
        if isinstance((method := await self.__app.notify(update, bot)), TelegramMethod):
            await bot(method)

    async def _listen_updates(self, token: str):
        async with Bot(
            token=token, presets=self.__app.presets, api=self.__app.api
        ) as bot:
            offset = 0
            while self.__running:
                if updates := await bot.get_updates(offset=offset, timeout=5):
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
