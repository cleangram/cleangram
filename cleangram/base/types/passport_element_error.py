from __future__ import annotations

from dataclasses import dataclass

from .base import TelegramType


@dataclass
class PassportElementError(TelegramType):
    """
    This object represents an error in the Telegram Passport
    element which was submitted that should be resolved by the
    user. It should be one of:

        - PassportElementErrorDataField
        - PassportElementErrorFrontSide
        - PassportElementErrorReverseSide
        - PassportElementErrorSelfie
        - PassportElementErrorFile
        - PassportElementErrorFiles
        - PassportElementErrorTranslationFile
        - PassportElementErrorTranslationFiles
        - PassportElementErrorUnspecified

    Reference: https://core.telegram.org/bots/api#passportelementerror
    """
