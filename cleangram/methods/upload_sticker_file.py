from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from ..types import File, InputFile, Response
from .base import TelegramMethod

from ..utils import Presets, attach


@dataclass
class UploadStickerFile(TelegramMethod, response=Response[File]):
    """
    Use this method to upload a .PNG file with a sticker for
    later use in createNewStickerSet and addStickerToSet methods
    (can be used multiple times). Returns the uploaded File on
    success.

    Reference: https://core.telegram.org/bots/api#uploadstickerfile
    """

    user_id: int
    """User identifier of sticker file owner"""

    png_sticker: InputFile
    """PNG image with the sticker, must be up to 512 kilobytes in
    size, dimensions must not exceed 512px, and either width or
    height must be exactly 512px. More info on Sending Files »"""

    def preset(self, presets: Presets) -> Dict[str, InputFile]:
        files = super(UploadStickerFile, self).preset(presets)
        self.png_sticker = attach(self.png_sticker, files)
        return files
