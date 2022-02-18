from dataclasses import dataclass, field

from ...base.methods import TelegramMethod
from ...utils import env


@dataclass
class Api:
    url: str = field(default=env.TG_API)
    local: bool = field(default=env.TG_LOCAL)

    def base_url(self, token: str, call: TelegramMethod):
        u = f"{self.url}/bot{token}/{call.__method__}"
        print(u)
        return u
