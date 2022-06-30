from ...core.objects.response import Response
from ...core.paths.send_location import SendLocation as _SendLocation
from ..objects import Message


class SendLocation(_SendLocation, response=Response[Message]):
    """
    Use this method to send point on the map. On success, the sent Message
    is returned.

    Reference: https://core.telegram.org/bots/api#sendlocation
    """
