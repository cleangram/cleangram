from ...core.objects.response import Response
from ...core.paths.send_document import SendDocument as _SendDocument
from ..objects import Message


class SendDocument(_SendDocument, response=Response[Message]):
    """
    Use this method to send general files. On success, the sent Message is
    returned. Bots can currently send files of any type of up to 50 MB in
    size, this limit may be changed in the future.

    Reference: https://core.telegram.org/bots/api#senddocument
    """
