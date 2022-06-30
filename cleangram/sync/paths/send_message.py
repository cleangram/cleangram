from ...core.objects.response import Response
from ...core.paths.send_message import SendMessage as _SendMessage
from ..objects import Message


class SendMessage(_SendMessage, response=Response[Message]):
    """
    Use this method to send text messages. On success, the sent Message is
    returned.

    Reference: https://core.telegram.org/bots/api#sendmessage
    """
