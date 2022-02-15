import os
from dataclasses import dataclass, fields


@dataclass(frozen=True)
class _Env:
    TELEGRAM_BOT_TOKEN: str = ""
    TELEGRAM_BOT_API: str = "https://api.telegram.org"
    WEBHOOK_ENDPOINT: str = ""


env = _Env(**{f.name: os.environ[f.name] for f in fields(_Env) if f.name in os.environ})
