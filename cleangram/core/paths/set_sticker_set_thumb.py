from typing import Union

from ...core.objects.response import Response
from ..bot.bot import Bot
from ..objects import InputFile
from .base import TelegramPath


class SetStickerSetThumb(TelegramPath, response=Response[bool]):
    """
    Use this method to set the thumbnail of a sticker set. Animated
    thumbnails can be set for animated sticker sets only. Video thumbnails
    can be set only for video sticker sets only. Returns True on success.
    The following methods and objects allow your bot to work in inline
    mode.Please see our Introduction to Inline bots for more details.
    To enable this option, send the /setinline command to @BotFather and
    provide the placeholder text that the user will see in the input field
    after typing your bot's name.

    Reference: https://core.telegram.org/bots/api#setstickersetthumb
    """

    name: str
    """Sticker set name"""

    user_id: int
    """User identifier of the sticker set owner"""

    thumb: Union[None, InputFile, str] = None
    """A PNG image with the thumbnail, must be up to 128 kilobytes in size
    and have width and height exactly 100px, or a TGS animation with the
    thumbnail up to 32 kilobytes in size; see
    https://core.telegram.org/stickers#animated-sticker-requirements for
    animated sticker technical requirements, or a WEBM video with the
    thumbnail up to 32 kilobytes in size; see
    https://core.telegram.org/stickers#video-sticker-requirements for
    video sticker technical requirements. Pass a file_id as a String to
    send a file that already exists on the Telegram servers, pass an HTTP
    URL as a String for Telegram to get a file from the Internet, or
    upload a new one using multipart/form-data. More information on
    Sending Files ». Animated sticker set thumbnails can't be uploaded via
    HTTP URL."""

    def prepare(self, bot: Bot):
        self.attach(self.thumb, 'thumb')
