from ...core.objects.response import Response
from ...core.paths.send_photo import SendPhoto as _SendPhoto
from ..objects import Message


class SendPhoto(_SendPhoto, response=Response[Message]):
    """
    Use this method to send photos. On success, the sent Message is
    returned.

    Reference: https://core.telegram.org/bots/api#sendphoto
    """
