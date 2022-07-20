from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Any, Optional, Type

if TYPE_CHECKING:
    from ..http import Http
    from .config import BotConfig
    from ..objects import User
    from ..paths import TelegramPath

from ..http import Http


class Bot(abc.ABC):
    """
    Client instance for work with Telegram Bot API
    """

    __http__: Type[Http]

    @property
    @abc.abstractmethod
    def token(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def config(self) -> BotConfig:
        ...

    @property
    @abc.abstractmethod
    def me(self) -> User:
        ...

    @property
    @abc.abstractmethod
    def id(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def http(self) -> Http:
        ...

    @abc.abstractmethod
    def __call__(
        self, path: TelegramPath, http_timeout: Optional[float] = None
    ):
        ...

    @abc.abstractmethod
    def update_me(self):
        ...

    @abc.abstractmethod
    def cleanup(self):
        ...

    @abc.abstractmethod
    def get_me(self, http_timeout: Optional[float] = None) -> Any:
        """
        A simple method for testing your bot's authentication token. Requires
        no parameters. Returns basic information about the bot in form of a
        User object.

        :param http_timeout: (float)

        :returns: User

        Reference: https://core.telegram.org/bots/api#getme
        """
        ...

    @abc.abstractmethod
    def base_url(self, path: TelegramPath) -> str:
        pass
