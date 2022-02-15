from asyncio import Task

from typing import List, TYPE_CHECKING

import asyncio
import logging

from ...application.blueprint import Blueprint
from ...client import Bot
from ...methods import TelegramMethod
from ...utils import Presets

log = logging.getLogger(__name__)


class Polling:
    def __init__(self, blueprint: Blueprint, presets: Presets) -> None:
        self.__running: bool = False
        self.__blueprint: Blueprint = blueprint
        self.__presets: Presets = presets
        self.__log: logging.Logger = logging.getLogger("polling")

    async def start(self, *tokens: str):
        self.__running = True
        try:
            await self.__blueprint.startup.notify()
            await asyncio.gather(*map(self._listen_updates, tokens))
        finally:
            await self.__blueprint.shutdown.notify()

    async def notify(self, update, bot):
        if isinstance(
            (method := await self.__blueprint.notify(update, bot)), TelegramMethod
        ):
            await bot(method)

    async def _listen_updates(self, token: str):
        async with Bot(token) as bot:
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
            self.__log.info("Shutdown")
