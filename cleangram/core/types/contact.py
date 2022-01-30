from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .base import TelegramType


@dataclass
class Contact(TelegramType):
    """
    This object represents a phone contact.
    Reference: https://core.telegram.org/bots/api#contact
    """

    phone_number: str
    """Contact's phone number"""

    first_name: str
    """Contact's first name"""

    last_name: Optional[str] = field(default=None)
    """Optional. Contact's last name"""

    user_id: Optional[int] = field(default=None)
    """Optional. Contact's user identifier in Telegram. This number
    may have more than 32 significant bits and some programming
    languages may have difficulty/silent defects in interpreting
    it. But it has at most 52 significant bits, so a 64-bit
    integer or double-precision float type are safe for storing
    this identifier."""

    vcard: Optional[str] = field(default=None)
    """Optional. Additional data about the contact in the form of a
    vCard"""
