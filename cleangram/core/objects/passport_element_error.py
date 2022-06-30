from __future__ import annotations

from .base import TelegramObject


class PassportElementError(TelegramObject):
    """
    This object represents an error in the Telegram Passport element which
    was submitted that should be resolved by the user. It should be one
    of:

        :class:`cleangram.PassportElementErrorDataField`
        :class:`cleangram.PassportElementErrorFrontSide`
        :class:`cleangram.PassportElementErrorReverseSide`
        :class:`cleangram.PassportElementErrorSelfie`
        :class:`cleangram.PassportElementErrorFile`
        :class:`cleangram.PassportElementErrorFiles`
        :class:`cleangram.PassportElementErrorTranslationFile`
        :class:`cleangram.PassportElementErrorTranslationFiles`
        :class:`cleangram.PassportElementErrorUnspecified`

    Reference: https://core.telegram.org/bots/api#passportelementerror
    """
