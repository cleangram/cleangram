from dataclasses import dataclass, field

from dataclass_factory import Factory, Schema

from .api import Api
from ..http.base import BaseHttp
from ...utils import Presets


@dataclass
class BotConfig:
    api: Api = field(default_factory=Api)
    presets: Presets = field(default_factory=Presets)
    http: BaseHttp = field(default=None)

    def __post_init__(self):
        self.factory = Factory(default_schema=Schema(omit_default=True))
