from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .encrypted_credentials import EncryptedCredentials
from .base import TelegramType
from .encrypted_passport_element import EncryptedPassportElement


@dataclass
class PassportData(TelegramType):
    """
    Contains information about Telegram Passport data shared
    with the bot by the user.
    Reference: https://core.telegram.org/bots/api#passportdata
    """

    data: List[EncryptedPassportElement]
    """Array with information about documents and other Telegram
    Passport elements that was shared with the bot"""

    credentials: EncryptedCredentials
    """Encrypted credentials required to decrypt the data"""
