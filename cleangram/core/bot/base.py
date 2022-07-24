import abc

from .bot import Bot
from .config import BotConfig
from ..http.base import Http
from ..objects import User
from ..paths import TelegramPath


class BaseBot(Bot, abc.ABC):
    def __init__(self, token: str, config: BotConfig = None):
        self.__token = token
        self.__config = config or BotConfig(http=self.__http__())
        self._me = User(
            id=int(token.split(":")[0]),
            is_bot=True,
            first_name="Bot"
        )

    @property
    def token(self) -> str:
        return self.__token

    @property
    def config(self) -> BotConfig:
        return self.__config

    @property
    def me(self) -> User:
        return self._me

    @property
    def id(self) -> int:
        return self._me.id

    @property
    def http(self) -> Http:
        return self.__config.http

    def base_url(self, path: TelegramPath) -> str:
        return f"{self.__config.url}/bot{self.__token}/{path.__class__.__name__}"

    def __repr__(self):
        return f"Bot({self.token.split(':')[0]})"
