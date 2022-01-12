from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Chat:
    """
    Reference: https://core.telegram.org/bots/api#chat
    """
    id: int
    type: str
    title: Optional[str] = None
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
