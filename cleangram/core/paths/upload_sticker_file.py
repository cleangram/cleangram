from ...core.objects.response import Response
from ..bot.bot import Bot
from ..objects import File, InputFile
from .base import TelegramPath


class UploadStickerFile(TelegramPath, response=Response[File]):
    """
    Use this method to upload a .PNG file with a sticker for later use in
    createNewStickerSet and addStickerToSet methods (can be used multiple
    times). Returns the uploaded File on success.

    Reference: https://core.telegram.org/bots/api#uploadstickerfile
    """

    user_id: int
    """User identifier of sticker file owner"""

    png_sticker: InputFile
    """PNG image with the sticker, must be up to 512 kilobytes in size,
    dimensions must not exceed 512px, and either width or height must be
    exactly 512px. More information on Sending Files »"""

    def prepare(self, bot: Bot):
        self.attach(self.png_sticker, 'png_sticker')
