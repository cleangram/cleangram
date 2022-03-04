from __future__ import annotations

from dataclasses import dataclass

from .base import TelegramType


@dataclass
class InputMessageContent(TelegramType):
    """
    This object represents the content of a message to be sent
    as a result of an inline query. Telegram clients currently
    support the following 5 types:

        - InputTextMessageContent
        - InputLocationMessageContent
        - InputVenueMessageContent
        - InputContactMessageContent
        - InputInvoiceMessageContent

    Reference: https://core.telegram.org/bots/api#inputmessagecontent
    """
