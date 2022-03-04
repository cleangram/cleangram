import abc


class BaseEventObserver(abc.ABC):
    @abc.abstractmethod
    def attach(self, event): ...

    @abc.abstractmethod
    def __call__(self, event): ...

    @abc.abstractmethod
    async def notify(self, **kwargs): ...
