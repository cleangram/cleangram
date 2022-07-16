from __future__ import annotations

import typing
from dataclasses import dataclass
if typing.TYPE_CHECKING:
    from ..core.http.base import Http


@dataclass(frozen=True)
class BotConfig:
    http: Http
    api_url: str = "https://api.telegram.org"
