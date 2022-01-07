from dataclasses import dataclass
from typing import Optional

from .message import Message


@dataclass
class Update:
    update_id: int
    message: Optional[Message] = None
