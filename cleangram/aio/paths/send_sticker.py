from ...core.objects.response import Response
from ...core.paths.send_sticker import SendSticker as _SendSticker
from ..objects import Message


class SendSticker(_SendSticker, response=Response[Message]):
    """
    Use this method to send static .WEBP, animated .TGS, or video .WEBM
    stickers. On success, the sent Message is returned.

    Reference: https://core.telegram.org/bots/api#sendsticker
    """
