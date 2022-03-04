from __future__ import annotations

import functools
import inspect
from typing import TypeVar, TYPE_CHECKING, Type

from ..utils import check_filters
from ....base import TelegramType
from ....base.app.blueprint import BaseBlueprint
from ....base.app.observers import BaseHandlerObserver
from .manager import ContextManagerObserver


E = TypeVar("E")


class HandlerObserver(BaseHandlerObserver):
    def __init__(
        self,
        owner: BaseBlueprint,
        event_type: Type[TelegramType]
    ):
        self.__owner = owner
        self.middleware: ContextManagerObserver = ContextManagerObserver()
        self.__handlers: list = []
        self.__event: Type[TelegramType] = event_type

    def __call__(self, *filters, **flags):
        def func(handler):
            self.attach(handler, *filters, **flags)
            return handler

        return func

    def attach(self, handler, *filters, **flags):
        self.__handlers.append((handler, filters, flags))
        return handler

    async def notify(self, event: E, **kwargs):
        for handler, filters, flags in self.__handlers:
            if (
                fil_kwargs := await check_filters(event, filters, **kwargs)
            ) is not None:
                async with self.middleware.notify(event, **kwargs) as mw_args:
                    handler = functools.partial(handler, **kwargs, **mw_args, **fil_kwargs)
                    if processed := handler(event):
                        if inspect.iscoroutine(processed):
                            processed = await processed
                        return processed
                return True
