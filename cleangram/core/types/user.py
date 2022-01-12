from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    """
    Reference: https://core.telegram.org/bots/api#user
    """
    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    language_code: Optional[str] = None
    can_join_groups: Optional[bool] = None
    can_read_all_group_messages: Optional[bool] = None
    supports_inline_queries: Optional[bool] = None
