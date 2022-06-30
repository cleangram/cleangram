from typing import List

from ...core.objects.response import Response
from ...core.paths.send_media_group import SendMediaGroup as _SendMediaGroup
from ..objects import Message


class SendMediaGroup(_SendMediaGroup, response=Response[List[Message]]):
    """
    Use this method to send a group of photos, videos, documents or audios
    as an album. Documents and audio files can be only grouped in an album
    with messages of the same type. On success, an array of Messages that
    were sent is returned.

    Reference: https://core.telegram.org/bots/api#sendmediagroup
    """
