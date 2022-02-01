from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, List

from cleangram.types import (
    Response,
    ShippingOption
)
from .base import TelegramMethod


@dataclass
class AnswerShippingQuery(TelegramMethod, response=Response[bool]):
    """
    If you sent an invoice requesting a shipping address and the
    parameter is_flexible was specified, the Bot API will send
    an Update with a shipping_query field to the bot. Use this
    method to reply to shipping queries. On success, True is
    returned.

    Reference: https://core.telegram.org/bots/api#answershippingquery
    """

    shipping_query_id: str
    """Unique identifier for the query to be answered"""

    ok: bool
    """Specify True if delivery to the specified address is
    possible and False if there are any problems (for example,
    if delivery to the specified address is not possible)"""

    shipping_options: Optional[List[ShippingOption]] = field(default=None)
    """Required if ok is True. A JSON-serialized array of available
    shipping options."""

    error_message: Optional[str] = field(default=None)
    """Required if ok is False. Error message in human readable
    form that explains why it is impossible to complete the
    order (e.g. "Sorry, delivery to your desired address is
    unavailable'). Telegram will display this message to the
    user."""
