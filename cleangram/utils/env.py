from typing import List, Optional

import os
from dataclasses import dataclass, fields, field


@dataclass(frozen=True)
class _Env:
    TG_TOKEN: str = ""
    TG_API: str = "https://api.telegram.org"
    TG_LOCAL: bool = field(default=False)
    TG_PARSE_MODE: Optional[str] = field(default=None)
    WEBHOOK_ENDPOINT: str = ""


env = _Env(**{f.name: os.environ[f.name] for f in fields(_Env) if f.name in os.environ})
