from dataclasses import dataclass, field

from ...base.methods import TelegramMethod
from ...utils import env


@dataclass
class Api:
    url: str = field(default=env.TG_API)
    local: bool = field(default=env.TG_LOCAL)

    def base_url(self, token: str, call: TelegramMethod):
        return f"{self.url}/bot{token}/{call.__method__}"
