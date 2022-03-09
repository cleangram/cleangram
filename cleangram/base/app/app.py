import abc

from .worker import BaseWorker
from .. import Update
from ..client.config import BotConfig


class BaseApp(abc.ABC):
    @abc.abstractmethod
    def create_bot(
        self,
        token: str,
        bot_config: BotConfig = None
    ): ...

    @property
    @abc.abstractmethod
    def polling(self): ...

    @property
    @abc.abstractmethod
    def webhook(self): ...

    @property
    def worker(self) -> BaseWorker:
        if self.webhook:
            return self.webhook
        return self.polling

    @abc.abstractmethod
    def notify(
        self,
        update: Update,
        bot,
        **kwargs
    ): ...
