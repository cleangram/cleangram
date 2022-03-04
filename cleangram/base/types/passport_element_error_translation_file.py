from __future__ import annotations

from dataclasses import dataclass, field

from .passport_element_error import PassportElementError


@dataclass
class PassportElementErrorTranslationFile(PassportElementError):
    """
    Represents an issue with one of the files that constitute
    the translation of a document. The error is considered
    resolved when the file changes.
    Reference: https://core.telegram.org/bots/api#passportelementerrortranslationfile
    """

    type_: str
    """Type of element of the user's Telegram Passport which has
    the issue, one of “passport”, “driver_license”,
    “identity_card”, “internal_passport”, “utility_bill”,
    “bank_statement”, “rental_agreement”,
    “passport_registration”, “temporary_registration”"""

    file_hash: str
    """Base64-encoded file hash"""

    message: str
    """Error message"""

    source: str = field(default="")
    """Error source, must be translation_file"""

    def __post_init__(self):
        self.source = "translation_file"
