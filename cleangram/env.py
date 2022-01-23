from dataclasses import dataclass, fields
import os
from typing import Optional


@dataclass(frozen=True)
class _Env:
    TELEGRAM_BOT_TOKEN: Optional[str] = ""
    TELEGRAM_API_ENDPOINT: str = "https://api.telegram.org"
    WEBHOOK_ENDPOINT: str = ""


env = _Env(**{f.name: os.environ[f.name] for f in fields(_Env)
              if f.name in os.environ})
