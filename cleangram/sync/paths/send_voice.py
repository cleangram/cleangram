from ...core.objects.response import Response
from ...core.paths.send_voice import SendVoice as _SendVoice
from ..objects import Message


class SendVoice(_SendVoice, response=Response[Message]):
    """
    Use this method to send audio files, if you want Telegram clients to
    display the file as a playable voice message. For this to work, your
    audio must be in an .OGG file encoded with OPUS (other formats may be
    sent as Audio or Document). On success, the sent Message is returned.
    Bots can currently send voice messages of up to 50 MB in size, this
    limit may be changed in the future.

    Reference: https://core.telegram.org/bots/api#sendvoice
    """
