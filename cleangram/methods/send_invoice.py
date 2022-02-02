from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Union

from ..types import (
    InlineKeyboardMarkup,
    LabeledPrice,
    Message,
    Response
)
from .base import TelegramMethod


@dataclass
class SendInvoice(TelegramMethod, response=Response[Message]):
    """
    Use this method to send invoices. On success, the sent
    Message is returned.

    Reference: https://core.telegram.org/bots/api#sendinvoice
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    title: str
    """Product name, 1-32 characters"""

    description: str
    """Product description, 1-255 characters"""

    payload: str
    """Bot-defined invoice payload, 1-128 bytes. This will not be
    displayed to the user, use for your internal processes."""

    provider_token: str
    """Payments provider token, obtained via Botfather"""

    currency: str
    """Three-letter ISO 4217 currency code, see more on currencies"""

    prices: List[LabeledPrice]
    """Price breakdown, a JSON-serialized list of components (e.g.
    product price, tax, discount, delivery cost, delivery tax,
    bonus, etc.)"""

    max_tip_amount: Optional[int] = field(default=None)
    """The maximum accepted amount for tips in the smallest units
    of the currency (integer, not float/double). For example,
    for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See
    the exp parameter in currencies.json, it shows the number of
    digits past the decimal point for each currency (2 for the
    majority of currencies). Defaults to 0"""

    suggested_tip_amounts: Optional[List[int]] = field(default=None)
    """A JSON-serialized array of suggested amounts of tips in the
    smallest units of the currency (integer, not float/double).
    At most 4 suggested tip amounts can be specified. The
    suggested tip amounts must be positive, passed in a strictly
    increased order and must not exceed max_tip_amount."""

    start_parameter: Optional[str] = field(default=None)
    """Unique deep-linking parameter. If left empty, forwarded
    copies of the sent message will have a Pay button, allowing
    multiple users to pay directly from the forwarded message,
    using the same invoice. If non-empty, forwarded copies of
    the sent message will have a URL button with a deep link to
    the bot (instead of a Pay button), with the value used as
    the start parameter"""

    provider_data: Optional[str] = field(default=None)
    """A JSON-serialized data about the invoice, which will be
    shared with the payment provider. A detailed description of
    required fields should be provided by the payment provider."""

    photo_url: Optional[str] = field(default=None)
    """URL of the product photo for the invoice. Can be a photo of
    the goods or a marketing image for a service. People like it
    better when they see what they are paying for."""

    photo_size: Optional[int] = field(default=None)
    """Photo size"""

    photo_width: Optional[int] = field(default=None)
    """Photo width"""

    photo_height: Optional[int] = field(default=None)
    """Photo height"""

    need_name: Optional[bool] = field(default=None)
    """Pass True, if you require the user's full name to complete
    the order"""

    need_phone_number: Optional[bool] = field(default=None)
    """Pass True, if you require the user's phone number to
    complete the order"""

    need_email: Optional[bool] = field(default=None)
    """Pass True, if you require the user's email address to
    complete the order"""

    need_shipping_address: Optional[bool] = field(default=None)
    """Pass True, if you require the user's shipping address to
    complete the order"""

    send_phone_number_to_provider: Optional[bool] = field(default=None)
    """Pass True, if user's phone number should be sent to provider"""

    send_email_to_provider: Optional[bool] = field(default=None)
    """Pass True, if user's email address should be sent to
    provider"""

    is_flexible: Optional[bool] = field(default=None)
    """Pass True, if the final price depends on the shipping method"""

    disable_notification: Optional[bool] = field(default=None)
    """Sends the message silently. Users will receive a
    notification with no sound."""

    protect_content: Optional[bool] = field(default=None)
    """Protects the contents of the sent message from forwarding
    and saving"""

    reply_to_message_id: Optional[int] = field(default=None)
    """If the message is a reply, ID of the original message"""

    allow_sending_without_reply: Optional[bool] = field(default=None)
    """Pass True, if the message should be sent even if the
    specified replied-to message is not found"""

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """A JSON-serialized object for an inline keyboard. If empty,
    one 'Pay total price' button will be shown. If not empty,
    the first button must be a Pay button."""
