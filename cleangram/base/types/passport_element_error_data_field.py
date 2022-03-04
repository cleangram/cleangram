from __future__ import annotations

from dataclasses import dataclass, field

from .passport_element_error import PassportElementError


@dataclass
class PassportElementErrorDataField(PassportElementError):
    """
    Represents an issue in one of the data fields that was
    provided by the user. The error is considered resolved when
    the field's value changes.
    Reference: https://core.telegram.org/bots/api#passportelementerrordatafield
    """

    type_: str
    """The section of the user's Telegram Passport which has the
    error, one of “personal_details”, “passport”,
    “driver_license”, “identity_card”, “internal_passport”,
    “address”"""

    field_name: str
    """Name of the data field which has the error"""

    data_hash: str
    """Base64-encoded data hash"""

    message: str
    """Error message"""

    source: str = field(default="")
    """Error source, must be data"""

    def __post_init__(self):
        self.source = "data"
