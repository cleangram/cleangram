from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .base import TelegramType


@dataclass
class ResponseParameters(TelegramType):
    """
    Contains information about why a request was unsuccessful.
    Reference: https://core.telegram.org/bots/api#responseparameters
    """

    migrate_to_chat_id: Optional[int] = field(default=None)
    """Optional. The group has been migrated to a supergroup with
    the specified identifier. This number may have more than 32
    significant bits and some programming languages may have
    difficulty/silent defects in interpreting it. But it has at
    most 52 significant bits, so a signed 64-bit integer or
    double-precision float type are safe for storing this
    identifier."""

    retry_after: Optional[int] = field(default=None)
    """Optional. In case of exceeding flood control, the number of
    seconds left to wait before the request can be repeated"""
