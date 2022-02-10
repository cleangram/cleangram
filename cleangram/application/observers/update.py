from typing import Any, Callable, Generic, List, TypeVar

from cleangram.application.observers.base import Observer

from ...client import Bot

U = TypeVar("U")


class UpdateObserver(Observer, Generic[U]):
    def __init__(self):
        self._handlers: List[Callable[[U, Any], Any]] = []

    def __call__(self, handler: Callable[[U, Any], Any]):
        self._handlers.append(handler)

    async def notify(self, event: U, bot: Bot):
        for handler in self._handlers:
            if resp := await handler(event, bot):
                return resp
