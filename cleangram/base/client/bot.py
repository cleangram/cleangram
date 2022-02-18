from typing import Dict

import abc
from dataclass_factory import Factory, Schema

from dataclasses import dataclass, field, InitVar

from .api import Api
from cleangram.base.http.request import Request
from ..methods import TelegramMethod
from ...utils import env, Presets
from ...exceptions import InvalidToken, check


@dataclass
class BaseBot(abc.ABC):
    token: InitVar[str] = field(repr=False)
    presets: Presets = field(default_factory=Presets)
    api: Api = field(default_factory=Api)

    def __post_init__(self, token: str = env.TG_TOKEN):
        if not token:
            raise InvalidToken
        self.__token = token
        self.__factory = Factory(default_schema=Schema(omit_default=True))

    def _build_request(self, call: TelegramMethod, timeout: float) -> Request:
        return Request(
            url=self.api.base_url(self.__token, call),
            files=call.preset(self.presets),
            data=self.__factory.dump(call),
            timeout=timeout,
        )

    def _build_result(self, raw: Dict, call: TelegramMethod):
        return check(self.__factory.load(raw, call.__response__)).result

    @property
    def factory(self):
        return self.__factory
