from __future__ import annotations

from dataclasses import dataclass, field, InitVar


from .passport_element_error import PassportElementError


@dataclass
class PassportElementErrorUnspecified(PassportElementError):
    """
    Represents an issue in an unspecified place. The error is
    considered resolved when new data is added.
    Reference: https://core.telegram.org/bots/api#passportelementerrorunspecified
    """

    type_: str
    """Type of element of the user's Telegram Passport which has
    the issue"""

    element_hash: str
    """Base64-encoded element hash"""

    message: str
    """Error message"""

    source: str = field(default="unspecified")
    """Error source, must be unspecified"""
