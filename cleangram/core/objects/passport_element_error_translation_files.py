from __future__ import annotations

from typing import List

from pydantic import Field

from .passport_element_error import PassportElementError


class PassportElementErrorTranslationFiles(PassportElementError):
    """
    Represents an issue with the translated version of a document. The
    error is considered resolved when a file with the document translation
    change.

    Reference: https://core.telegram.org/bots/api#passportelementerrortranslationfiles
    """

    type: str
    """Type of element of the user's Telegram Passport which has the issue,
    one of “passport”, “driver_license”, “identity_card”,
    “internal_passport”, “utility_bill”, “bank_statement”,
    “rental_agreement”, “passport_registration”, “temporary_registration”"""

    file_hashes: List[str] = Field(default_factory=list)
    """List of base64-encoded file hashes"""

    message: str
    """Error message"""

    source: str = 'translation_files'
    """Error source, must be translation_files"""
