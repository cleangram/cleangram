from __future__ import annotations

from dataclasses import dataclass, field, InitVar


from .passport_element_error import PassportElementError


@dataclass
class PassportElementErrorFrontSide(PassportElementError):
    """
    Represents an issue with the front side of a document. The
    error is considered resolved when the file with the front
    side of the document changes.
    Reference: https://core.telegram.org/bots/api#passportelementerrorfrontside
    """

    type_: str
    """The section of the user's Telegram Passport which has the
    issue, one of “passport”, “driver_license”, “identity_card”,
    “internal_passport”"""

    file_hash: str
    """Base64-encoded hash of the file with the front side of the
    document"""

    message: str
    """Error message"""

    source: str = field(default='')
    """Error source, must be front_side"""

    def __post_init__(self):
        self.source = "front_side"
    