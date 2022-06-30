from __future__ import annotations

from .passport_element_error import PassportElementError


class PassportElementErrorSelfie(PassportElementError):
    """
    Represents an issue with the selfie with a document. The error is
    considered resolved when the file with the selfie changes.

    Reference: https://core.telegram.org/bots/api#passportelementerrorselfie
    """

    type: str
    """The section of the user's Telegram Passport which has the issue, one
    of “passport”, “driver_license”, “identity_card”, “internal_passport”"""

    file_hash: str
    """Base64-encoded hash of the file with the selfie"""

    message: str
    """Error message"""

    source: str = 'selfie'
    """Error source, must be selfie"""
