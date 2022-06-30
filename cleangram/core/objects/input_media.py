from __future__ import annotations

from .base import TelegramObject


class InputMedia(TelegramObject):
    """
    This object represents the content of a media message to be sent. It
    should be one of

        :class:`cleangram.InputMediaAnimation`
        :class:`cleangram.InputMediaDocument`
        :class:`cleangram.InputMediaAudio`
        :class:`cleangram.InputMediaPhoto`
        :class:`cleangram.InputMediaVideo`

    Reference: https://core.telegram.org/bots/api#inputmedia
    """
