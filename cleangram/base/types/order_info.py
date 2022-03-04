from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .base import TelegramType
from .shipping_address import ShippingAddress


@dataclass
class OrderInfo(TelegramType):
    """
    This object represents information about an order.
    Reference: https://core.telegram.org/bots/api#orderinfo
    """

    name: Optional[str] = field(default=None)
    """Optional. User name"""

    phone_number: Optional[str] = field(default=None)
    """Optional. User's phone number"""

    email: Optional[str] = field(default=None)
    """Optional. User email"""

    shipping_address: Optional[ShippingAddress] = field(default=None)
    """Optional. User shipping address"""
