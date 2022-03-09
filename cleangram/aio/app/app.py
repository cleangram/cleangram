import logging
from typing import Union

from dataclass_factory import Factory
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

from .webhook import Webhook
from ...base import Update, TelegramMethod
from ...base.app.app import BaseApp
from ...base.client.config import BotConfig
from ..client.bot import Bot
from ..http.httpx_ import HttpX
from .blueprint import Blueprint
from .polling import Polling
from ...utils.event_type import get_event_and_type


class App(BaseApp, Blueprint):
    def __init__(
        self,
        name: str = "app",
        *args,
        bot_config: BotConfig = None,
        **kwargs
    ) -> None:
        self.__bot_config = bot_config or BotConfig(HttpX())
        super(App, self).__init__(name, *args, **kwargs)
        self.__polling = Polling(self)
        self.__webhook = Webhook(self)

    @property
    def polling(self) -> Polling:
        return self.__polling

    @property
    def webhook(self) -> Webhook:
        return self.__webhook

    def create_bot(self, token: str, config: BotConfig = None) -> Bot:
        return Bot(token, config or self.__bot_config)

    async def notify(self, update: Update, bot: Bot, **kwargs) -> Union[TelegramMethod, bool]:
        event, type_ = get_event_and_type(update)
        return await self._notify(update, event, type_, bot=bot, **kwargs)

    # @property
    # def starlette(self):
    #     async def root(request: Request):
    #         async with self.create_bot(request.path_params["bot"]) as bot:
    #             return JSONResponse(
    #                 await self.notify(
    #                     bot.factory.load(await request.json(), Update), bot
    #                 )
    #             )
    #
    #     return Starlette(
    #         routes=[Route("/bot{bot}", root, methods=["POST"])],
    #         # on_startup=[self.emit_startup],
    #         # on_shutdown=[self.emit_shutdown]
    #     )
