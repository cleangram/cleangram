from dataclasses import dataclass

import functools

from typing import Any, Callable, Generic, List, TypeVar, Awaitable, Tuple

from .base import Observer

from ...client import Bot

U = TypeVar("U")


@dataclass
class Handler:
    name: str
    handler: Callable
    filters: Any


class HandlerObserver(Observer, Generic[U]):
    def __init__(self):
        self.__handlers: List = []

    def __call__(self, *filters):
        def wrap(handler):
            return self.append(handler, *filters)

        return wrap

    def append(self, handler: Callable, *filters, **kwargs):
        self.__handlers.append(
            Handler(name=handler.__name__, handler=handler, filters=filters)
        )
        return handler

    async def notify(self, event: U, bot: Bot):
        for handler in self.__handlers:
            if all([f(event) for f in handler.filters]):
                return await handler.handler(event, bot) or True
