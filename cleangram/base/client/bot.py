import abc
from typing import Dict, Type

from .config import BotConfig
from .. import User
from ..http.base import BaseHttp
from ...base.http.request import Request

from ...exceptions import InvalidToken, check
from ..methods import TelegramMethod


class BaseBot(abc.ABC):
    __http__: Type[BaseHttp]

    def __init__(
        self,
        token: str,
        config: BotConfig = None,
        me: User = None
    ):
        if not token:
            raise InvalidToken("Token not found")
        self.__token = token
        self._me = me or User(int(token.split(":")[0]), True, "bot")
        self._config = config or BotConfig(
            http=self.__http__()
        )

    def _build_request(self, call: TelegramMethod, timeout: float) -> Request:
        print(type(call))
        print(data := self._config.factory.dump(call))

        return Request(
            url=self._config.api.base_url(self.__token, call),
            files=call.preset(self._config.presets),
            data=data,
            timeout=timeout,
        )

    def _build_result(self, raw: Dict, call: TelegramMethod):
        return check(self._config.factory.load(raw, call.__response__)).result

    @property
    def token(self) -> str:
        return self.__token

    @property
    def me(self) -> User:
        return self._me

    @me.setter
    def me(self, _me: User) -> None:
        self._me = _me

    @property
    def id(self) -> int:
        return self._me.id

    @property
    def http(self):
        return self._config.http
