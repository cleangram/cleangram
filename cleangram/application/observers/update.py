from typing import Generic, TypeVar, List, Callable, Any

from ...client import Bot
from cleangram.application.observers.base import Observer

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
