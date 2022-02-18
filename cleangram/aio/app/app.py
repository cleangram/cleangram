import logging

from .blueprint import Blueprint
from .polling import Polling
from .. import Bot
from ..http.base import AioHttp
from ..http.httpx_ import HttpX
from ...base.client.api import Api
from ...aio.types import Update
from ...utils import Presets

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.routing import Route


class App(Blueprint):
    def __init__(
        self,
        name: str = "app",
        presets: Presets = None,
        api: Api = Api(),
        http: AioHttp = HttpX(),
        **kwargs
    ) -> None:
        self.name = name
        self.log = logging.getLogger(name)
        self.presets = presets or Presets()
        self.api = api
        self.http = http
        super(App, self).__init__(**kwargs)

    @property
    def polling(self):
        return Polling(self)

    @property
    def starlette(self):
        async def root(request: Request):
            async with Bot(
                request.path_params["bot"],
                presets=self.presets,
                http=self.http,
                api=self.api,
            ) as bot:
                return JSONResponse(
                    await self.notify(
                        bot.factory.load(await request.json(), Update), bot
                    )
                )

        return Starlette(
            routes=[Route("/bot{bot}", root, methods=["POST"])],
            on_startup=[self.emit_startup],
            on_shutdown=[self.emit_shutdown],
        )
