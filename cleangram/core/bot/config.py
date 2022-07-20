from dataclasses import dataclass
from ..http.http import Http


@dataclass(frozen=True)
class BotConfig:
    """
    Bot configs
    """
    http: Http
    """Default HTTP Client for make connections to API"""

    url: str = "https://api.telegram.org"
    """URL to Telegram Bot API server"""

    local: bool = False
    """is API server local"""
