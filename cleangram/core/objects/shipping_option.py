from __future__ import annotations

from typing import TYPE_CHECKING, List

from pydantic import Field

from .base import TelegramObject

if TYPE_CHECKING:
    from .labeled_price import LabeledPrice


class ShippingOption(TelegramObject):
    """
    This object represents one shipping option.

    Reference: https://core.telegram.org/bots/api#shippingoption
    """

    id: str
    """Shipping option identifier"""

    title: str
    """Option title"""

    prices: List[LabeledPrice] = Field(default_factory=list)
    """List of price portions"""
