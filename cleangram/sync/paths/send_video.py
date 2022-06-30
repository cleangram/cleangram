from ...core.objects.response import Response
from ...core.paths.send_video import SendVideo as _SendVideo
from ..objects import Message


class SendVideo(_SendVideo, response=Response[Message]):
    """
    Use this method to send video files, Telegram clients support MPEG4
    videos (other formats may be sent as Document). On success, the sent
    Message is returned. Bots can currently send video files of up to 50
    MB in size, this limit may be changed in the future.

    Reference: https://core.telegram.org/bots/api#sendvideo
    """
