from typing import Optional

from dataclasses import dataclass


@dataclass
class TelegramException(Exception):
    code: int
    description: Optional[str] = None


class Unauthorized(Exception):
    ...
