from __future__ import annotations

from dataclasses import dataclass

from .base import TelegramType
from .shipping_address import ShippingAddress
from .user import User


@dataclass
class ShippingQuery(TelegramType):
    """
    This object contains information about an incoming shipping
    query.
    Reference: https://core.telegram.org/bots/api#shippingquery
    """

    id: str
    """Unique query identifier"""

    from_: User
    """User who sent the query"""

    invoice_payload: str
    """Bot specified invoice payload"""

    shipping_address: ShippingAddress
    """User specified shipping address"""
