from __future__ import annotations

from dataclasses import dataclass, field, InitVar


from .passport_element_error import PassportElementError


@dataclass
class PassportElementErrorFile(PassportElementError):
    """
    Represents an issue with a document scan. The error is
    considered resolved when the file with the document scan
    changes.
    Reference: https://core.telegram.org/bots/api#passportelementerrorfile
    """

    type_: str
    """The section of the user's Telegram Passport which has the
    issue, one of “utility_bill”, “bank_statement”,
    “rental_agreement”, “passport_registration”,
    “temporary_registration”"""

    file_hash: str
    """Base64-encoded file hash"""

    message: str
    """Error message"""

    source: str = field(default="file")
    """Error source, must be file"""
