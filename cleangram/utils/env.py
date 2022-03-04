import os
from dataclasses import dataclass, field, fields
from typing import Optional


@dataclass
class _Env:
    TG_TOKEN: str = ""
    TG_API: str = "https://api.telegram.org"
    TG_LOCAL: bool = field(default=None)
    TG_PARSE_MODE: Optional[str] = field(default=None)
    WEBHOOK_ENDPOINT: str = ""

    def __post_init__(self):
        self.TG_LOCAL = self.TG_LOCAL in ("true", "1", "yes")


env = _Env(**{f.name: os.environ[f.name] for f in fields(_Env) if f.name in os.environ})
