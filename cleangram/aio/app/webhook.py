from __future__ import annotations

from typing import TYPE_CHECKING

from ...base import Update
from ...base.app.worker import Worker


if TYPE_CHECKING:
    from .app import App


class Webhook(Worker):
    def __init__(
        self,
        app: App
    ):
        self.__app = app
        self.__running = False

    def __bool__(self) -> bool:
        return self.__running

    def run(self) -> None:
        pass

    def start(self):
        pass

    def notify(self, update: Update, bot):
        pass
