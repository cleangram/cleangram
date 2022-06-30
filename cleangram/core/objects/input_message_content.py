from __future__ import annotations

from .base import TelegramObject


class InputMessageContent(TelegramObject):
    """
    This object represents the content of a message to be sent as a result
    of an inline query. Telegram clients currently support the following 5
    types:

        :class:`cleangram.InputTextMessageContent`
        :class:`cleangram.InputLocationMessageContent`
        :class:`cleangram.InputVenueMessageContent`
        :class:`cleangram.InputContactMessageContent`
        :class:`cleangram.InputInvoiceMessageContent`

    Reference: https://core.telegram.org/bots/api#inputmessagecontent
    """
