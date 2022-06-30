from ...core.objects.response import Response
from ...core.paths.send_video_note import SendVideoNote as _SendVideoNote
from ..objects import Message


class SendVideoNote(_SendVideoNote, response=Response[Message]):
    """
    As of v.4.0, Telegram clients support rounded square MPEG4 videos of
    up to 1 minute long. Use this method to send video messages. On
    success, the sent Message is returned.

    Reference: https://core.telegram.org/bots/api#sendvideonote
    """
