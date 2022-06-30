from ...core.objects.response import Response
from ...core.paths.send_poll import SendPoll as _SendPoll
from ..objects import Message


class SendPoll(_SendPoll, response=Response[Message]):
    """
    Use this method to send a native poll. On success, the sent Message is
    returned.

    Reference: https://core.telegram.org/bots/api#sendpoll
    """
