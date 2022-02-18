from __future__ import annotations

from dataclasses import dataclass


from .base import TelegramType


@dataclass
class InputMedia(TelegramType):
    """
    This object represents the content of a media message to be
    sent. It should be one of

        - InputMediaAnimation
        - InputMediaDocument
        - InputMediaAudio
        - InputMediaPhoto
        - InputMediaVideo

    Reference: https://core.telegram.org/bots/api#inputmedia
    """
