import abc
from dataclasses import InitVar, dataclass, field
from typing import Dict

from dataclass_factory import Factory, Schema

from .. import User
from ...base.http.request import Request

from ...exceptions import InvalidToken, check
from ...utils import Presets, env
from ..methods import TelegramMethod
from .api import Api


def dc_factory():
    return Factory(default_schema=Schema(omit_default=True))


@dataclass
class BaseBot(abc.ABC):
    _token: InitVar[str] = field(repr=False)
    presets: Presets = field(default_factory=Presets)
    api: Api = field(default_factory=Api)
    factory: Factory = field(default_factory=dc_factory)

    def __post_init__(self, _token: str = env.TG_TOKEN):
        if not _token:
            raise InvalidToken("Token not found")
        self.__token = _token
        self._me = User(0, True, "bot")

    def _build_request(self, call: TelegramMethod, timeout: float) -> Request:
        return Request(
            url=self.api.base_url(self.__token, call),
            files=call.preset(self.presets),
            data=self.factory.dump(call),
            timeout=timeout,
        )

    def _build_result(self, raw: Dict, call: TelegramMethod):
        return check(self.factory.load(raw, call.__response__)).result

    @property
    def token(self) -> str:
        return self.__token

    @property
    def me(self) -> User:
        return self._me
