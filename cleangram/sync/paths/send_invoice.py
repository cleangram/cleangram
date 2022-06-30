from ...core.objects.response import Response
from ...core.paths.send_invoice import SendInvoice as _SendInvoice
from ..objects import Message


class SendInvoice(_SendInvoice, response=Response[Message]):
    """
    Use this method to send invoices. On success, the sent Message is
    returned.

    Reference: https://core.telegram.org/bots/api#sendinvoice
    """
