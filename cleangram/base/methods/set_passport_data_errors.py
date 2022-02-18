from __future__ import annotations

from dataclasses import dataclass
from typing import List

from ..types import PassportElementError, Response
from .base import TelegramMethod


@dataclass
class SetPassportDataErrors(TelegramMethod, response=Response[bool]):
    """
    Informs a user that some of the Telegram Passport elements
    they provided contains errors. The user will not be able to
    re-submit their Passport to you until the errors are fixed
    (the contents of the field for which you returned the error
    must change). Returns True on success.

    Reference: https://core.telegram.org/bots/api#setpassportdataerrors
    """

    user_id: int
    """User identifier"""

    errors: List[PassportElementError]
    """A JSON-serialized array describing the errors"""
