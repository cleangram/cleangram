from typing import Union

from ...core.objects.response import Response
from ...core.paths.edit_message_media import (
    EditMessageMedia as _EditMessageMedia,
)
from ..objects import Message


class EditMessageMedia(
    _EditMessageMedia, response=Response[Union[bool, Message]]
):
    """
    Use this method to edit animation, audio, document, photo, or video
    messages. If a message is part of a message album, then it can be
    edited only to an audio for audio albums, only to a document for
    document albums and to a photo or a video otherwise. When an inline
    message is edited, a new file can't be uploaded; use a previously
    uploaded file via its file_id or specify a URL. On success, if the
    edited message is not an inline message, the edited Message is
    returned, otherwise True is returned.

    Reference: https://core.telegram.org/bots/api#editmessagemedia
    """
