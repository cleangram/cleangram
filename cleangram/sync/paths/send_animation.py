from ...core.objects.response import Response
from ...core.paths.send_animation import SendAnimation as _SendAnimation
from ..objects import Message


class SendAnimation(_SendAnimation, response=Response[Message]):
    """
    Use this method to send animation files (GIF or H.264/MPEG-4 AVC video
    without sound). On success, the sent Message is returned. Bots can
    currently send animation files of up to 50 MB in size, this limit may
    be changed in the future.

    Reference: https://core.telegram.org/bots/api#sendanimation
    """
