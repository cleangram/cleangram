from __future__ import annotations

from dataclasses import dataclass, field, InitVar
from typing import List, Optional, Union

from .input_file import InputFile
from .input_media import InputMedia
from .message_entity import MessageEntity


@dataclass
class InputMediaPhoto(InputMedia):
    """
    Represents a photo to be sent.
    Reference: https://core.telegram.org/bots/api#inputmediaphoto
    """

    media: Union[str, InputFile]
    """File to send. Pass a file_id to send a file that exists on
    the Telegram servers (recommended), pass an HTTP URL for
    Telegram to get a file from the Internet, or pass
    “attach://<file_attach_name>” to upload a new one using
    multipart/form-data under <file_attach_name> name. More info
    on Sending Files »"""

    caption: Optional[str] = field(default=None)
    """Optional. Caption of the photo to be sent, 0-1024 characters
    after entities parsing"""

    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the photo caption.
    See formatting options for more details."""

    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the
    caption, which can be specified instead of parse_mode"""

    type_: str = field(default='')
    """Type of the result, must be photo"""

    def __post_init__(self):
        self.type_ = "photo"
