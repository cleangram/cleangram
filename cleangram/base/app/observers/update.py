from typing import Generic, TypeVar

from .base import BaseObserver

T = TypeVar("T")


class UpdateObserver(BaseObserver, Generic[T]):
    def __init__(self):
        self.__handlers = []

    def __call__(self, *filters, **kwargs):
        def func(handler):
            self.attach(handler, *filters, **kwargs)

        return func

    def attach(self, handler, *filters, **kwargs):
        self.__handlers.append({handler, filters, kwargs})
        return handler

    def notify(self, bot, event: T):
        for handler, filters, kwargs in self.__handlers:
            if all([f(event) for f in filters]):
                return handler(event, bot, **kwargs)
