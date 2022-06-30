from ...core.objects.response import Response
from ...core.paths.send_venue import SendVenue as _SendVenue
from ..objects import Message


class SendVenue(_SendVenue, response=Response[Message]):
    """
    Use this method to send information about a venue. On success, the
    sent Message is returned.

    Reference: https://core.telegram.org/bots/api#sendvenue
    """
