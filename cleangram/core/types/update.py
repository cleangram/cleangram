from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .message import Message


@dataclass
class Update:
    """
    Reference: https://core.telegram.org/bots/api#update
    """
    update_id: int
    message: Optional[Message] = None
    edited_message: Optional[Message] = None
    channel_post: Optional[Message] = None
    edited_channel_post: Optional[Message] = None
