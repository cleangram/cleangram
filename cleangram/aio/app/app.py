import logging

from dataclass_factory import Factory
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

from .webhook import Webhook
from ..types import Update
from ...base.client.api import Api
from ...base.client.bot import dc_factory
from ...utils import Presets
from ..client.bot import Bot
from ..http.base import AioHttp
from ..http.httpx_ import HttpX
from .blueprint import Blueprint
from .polling import Polling


class App(Blueprint):
    def __init__(
        self,
        name: str = "app",
        *args,
        api: Api = Api(),
        factory: Factory = dc_factory(),
        http: AioHttp = HttpX(),
        presets: Presets = Presets(),
        **kwargs
    ) -> None:
        self.__presets = presets
        self.__api = api
        self.__http = http
        self.__factory = factory

        super(App, self).__init__(name, *args, **kwargs)

        self.__polling = Polling(self)
        self.__webhook = Webhook(self)

    def create_bot(self, token: str) -> Bot:
        return Bot(
            _token=token,
            presets=self.__presets,
            api=self.__api,
            factory=self.__factory,
            http=self.__http
        )

    @property
    def polling(self):
        return self.__polling

    @property
    def starlette(self):
        async def root(request: Request):
            async with self.create_bot(request.path_params["bot"]) as bot:
                return JSONResponse(
                    await self.notify(
                        bot.factory.load(await request.json(), Update), bot
                    )
                )

        return Starlette(
            routes=[Route("/bot{bot}", root, methods=["POST"])],
            # on_startup=[self.emit_startup],
            # on_shutdown=[self.emit_shutdown]
        )
