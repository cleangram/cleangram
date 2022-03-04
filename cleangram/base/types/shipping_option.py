from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .base import TelegramType
from .labeled_price import LabeledPrice


@dataclass
class ShippingOption(TelegramType):
    """
    This object represents one shipping option.
    Reference: https://core.telegram.org/bots/api#shippingoption
    """

    id: str
    """Shipping option identifier"""

    title: str
    """Option title"""

    prices: List[LabeledPrice]
    """List of price portions"""
