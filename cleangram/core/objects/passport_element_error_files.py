from __future__ import annotations

from typing import List

from pydantic import Field

from .passport_element_error import PassportElementError


class PassportElementErrorFiles(PassportElementError):
    """
    Represents an issue with a list of scans. The error is considered
    resolved when the list of files containing the scans changes.

    Reference: https://core.telegram.org/bots/api#passportelementerrorfiles
    """

    type: str
    """The section of the user's Telegram Passport which has the issue, one
    of “utility_bill”, “bank_statement”, “rental_agreement”,
    “passport_registration”, “temporary_registration”"""

    file_hashes: List[str] = Field(default_factory=list)
    """List of base64-encoded file hashes"""

    message: str
    """Error message"""

    source: str = 'files'
    """Error source, must be files"""
