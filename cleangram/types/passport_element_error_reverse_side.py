from __future__ import annotations

from dataclasses import dataclass, field, InitVar


from .passport_element_error import PassportElementError


@dataclass
class PassportElementErrorReverseSide(PassportElementError):
    """
    Represents an issue with the reverse side of a document. The
    error is considered resolved when the file with reverse side
    of the document changes.
    Reference: https://core.telegram.org/bots/api#passportelementerrorreverseside
    """

    type_: str
    """The section of the user's Telegram Passport which has the
    issue, one of “driver_license”, “identity_card”"""

    file_hash: str
    """Base64-encoded hash of the file with the reverse side of the
    document"""

    message: str
    """Error message"""

    source: str = field(default='')
    """Error source, must be reverse_side"""

    def __post_init__(self):
        self.source = "reverse_side"
    