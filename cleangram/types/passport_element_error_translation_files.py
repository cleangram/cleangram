from __future__ import annotations

from dataclasses import dataclass, field, InitVar
from typing import List

from .passport_element_error import PassportElementError


@dataclass
class PassportElementErrorTranslationFiles(PassportElementError):
    """
    Represents an issue with the translated version of a
    document. The error is considered resolved when a file with
    the document translation change.
    Reference: https://core.telegram.org/bots/api#passportelementerrortranslationfiles
    """

    type_: str
    """Type of element of the user's Telegram Passport which has
    the issue, one of “passport”, “driver_license”,
    “identity_card”, “internal_passport”, “utility_bill”,
    “bank_statement”, “rental_agreement”,
    “passport_registration”, “temporary_registration”"""

    file_hashes: List[str]
    """List of base64-encoded file hashes"""

    message: str
    """Error message"""

    source: str = field(default="translation_files")
    """Error source, must be translation_files"""
