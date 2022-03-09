import abc

from cleangram.base import Update


class BaseWorker(abc.ABC):

    @abc.abstractmethod
    def __bool__(self) -> bool: ...

    @abc.abstractmethod
    def run(self) -> None: ...

    @abc.abstractmethod
    def start(self): ...

    @abc.abstractmethod
    def notify(
        self,
        update: Update,
        bot,
    ): ...
