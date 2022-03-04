import abc

from .worker import Worker
from ..client.config import BotConfig


class BaseApp(abc.ABC):
    @abc.abstractmethod
    def create_bot(
        self,
        token: str,
        bot_config: BotConfig
    ): ...

    @property
    @abc.abstractmethod
    def polling(self): ...

    @property
    @abc.abstractmethod
    def webhook(self): ...

    @property
    def worker(self) -> Worker:
        if self.webhook:
            return self.webhook
        return self.polling
