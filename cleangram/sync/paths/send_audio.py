from ...core.objects.response import Response
from ...core.paths.send_audio import SendAudio as _SendAudio
from ..objects import Message


class SendAudio(_SendAudio, response=Response[Message]):
    """
    Use this method to send audio files, if you want Telegram clients to
    display them in the music player. Your audio must be in the .MP3 or
    .M4A format. On success, the sent Message is returned. Bots can
    currently send audio files of up to 50 MB in size, this limit may be
    changed in the future.
    For sending voice messages, use the sendVoice method instead.

    Reference: https://core.telegram.org/bots/api#sendaudio
    """
