import abc
from .base import BaseObserver


class BaseHandlerObserver(BaseObserver):
    @abc.abstractmethod
    def __call__(self, *filters, **flags): ...

    @abc.abstractmethod
    def attach(self, handler, *filters, **flags): ...

    @abc.abstractmethod
    def notify(self, event, bot, **kwargs): ...
