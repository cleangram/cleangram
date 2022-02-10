from __future__ import annotations

from dataclasses import dataclass, field, InitVar
from typing import List, Optional, Union

from .input_file import InputFile
from .input_media import InputMedia
from .message_entity import MessageEntity


@dataclass
class InputMediaAudio(InputMedia):
    """
    Represents an audio file to be treated as music to be sent.
    Reference: https://core.telegram.org/bots/api#inputmediaaudio
    """

    media: Union[str, InputFile]
    """File to send. Pass a file_id to send a file that exists on
    the Telegram servers (recommended), pass an HTTP URL for
    Telegram to get a file from the Internet, or pass
    “attach://<file_attach_name>” to upload a new one using
    multipart/form-data under <file_attach_name> name. More info
    on Sending Files »"""

    thumb: Optional[Union[InputFile, str]] = field(default=None)
    """Optional. Thumbnail of the file sent; can be ignored if
    thumbnail generation for the file is supported server-side.
    The thumbnail should be in JPEG format and less than 200 kB
    in size. A thumbnail's width and height should not exceed
    320. Ignored if the file is not uploaded using
    multipart/form-data. Thumbnails can't be reused and can be
    only uploaded as a new file, so you can pass
    “attach://<file_attach_name>” if the thumbnail was uploaded
    using multipart/form-data under <file_attach_name>. More
    info on Sending Files »"""

    caption: Optional[str] = field(default=None)
    """Optional. Caption of the audio to be sent, 0-1024 characters
    after entities parsing"""

    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the audio caption.
    See formatting options for more details."""

    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the
    caption, which can be specified instead of parse_mode"""

    duration: Optional[int] = field(default=None)
    """Optional. Duration of the audio in seconds"""

    performer: Optional[str] = field(default=None)
    """Optional. Performer of the audio"""

    title: Optional[str] = field(default=None)
    """Optional. Title of the audio"""

    type_: str = field(default='')
    """Type of the result, must be audio"""

    def __post_init__(self):
        self.type_ = "audio"
    