from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .base import TelegramType
from .order_info import OrderInfo
from .user import User


@dataclass
class PreCheckoutQuery(TelegramType):
    """
    This object contains information about an incoming pre-
    checkout query.
    Reference: https://core.telegram.org/bots/api#precheckoutquery
    """

    id: str
    """Unique query identifier"""

    from_: User
    """User who sent the query"""

    currency: str
    """Three-letter ISO 4217 currency code"""

    total_amount: int
    """Total price in the smallest units of the currency (integer,
    not float/double). For example, for a price of US$ 1.45 pass
    amount = 145. See the exp parameter in currencies.json, it
    shows the number of digits past the decimal point for each
    currency (2 for the majority of currencies)."""

    invoice_payload: str
    """Bot specified invoice payload"""

    shipping_option_id: Optional[str] = field(default=None)
    """Optional. Identifier of the shipping option chosen by the
    user"""

    order_info: Optional[OrderInfo] = field(default=None)
    """Optional. Order info provided by the user"""
