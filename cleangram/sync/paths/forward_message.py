from ...core.objects.response import Response
from ...core.paths.forward_message import ForwardMessage as _ForwardMessage
from ..objects import Message


class ForwardMessage(_ForwardMessage, response=Response[Message]):
    """
    Use this method to forward messages of any kind. Service messages
    can't be forwarded. On success, the sent Message is returned.

    Reference: https://core.telegram.org/bots/api#forwardmessage
    """
