import contextlib

import functools

import inspect

from typing import Generic, TypeVar

from ...client.bot import Bot

E = TypeVar("E")


class HandlerObserver(Generic[E]):
    def __init__(self):
        self.__handlers = []
        self.__middlewares = []

    def __call__(self, *filters, **flags):
        def func(handler):
            self.attach(handler, *filters, **flags)
            return handler

        return func

    def attach(self, handler, *filters, **flags):
        self.__handlers.append((handler, filters, flags))
        return handler

    async def notify(self, event: E, bot: Bot, mds):
        for handler, filters, flags in self.__handlers:
            if all(
                [
                    await f(event) if inspect.iscoroutinefunction(f) else f(event)
                    for f in filters
                ]
            ):
                async with contextlib.AsyncExitStack() as stack:  # type: contextlib.AsyncExitStack
                    mmds = [
                        await stack.enter_async_context(md())
                        for md in self.__middlewares
                    ]
                    handler = functools.partial(handler, **mds[0])
                    processed = handler(event, bot)
                    if inspect.iscoroutine(processed):
                        processed = await processed
                    return processed

    def middleware(self, gen):
        self.__middlewares.append(contextlib.asynccontextmanager(gen))
        return gen
