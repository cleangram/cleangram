from ...core.objects.response import Response
from ...core.paths.send_contact import SendContact as _SendContact
from ..objects import Message


class SendContact(_SendContact, response=Response[Message]):
    """
    Use this method to send phone contacts. On success, the sent Message
    is returned.

    Reference: https://core.telegram.org/bots/api#sendcontact
    """
