from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .input_message_content import InputMessageContent


@dataclass
class InputContactMessageContent(InputMessageContent):
    """
    Represents the content of a contact message to be sent as
    the result of an inline query.
    Reference: https://core.telegram.org/bots/api#inputcontactmessagecontent
    """

    phone_number: str
    """Contact's phone number"""

    first_name: str
    """Contact's first name"""

    last_name: Optional[str] = field(default=None)
    """Optional. Contact's last name"""

    vcard: Optional[str] = field(default=None)
    """Optional. Additional data about the contact in the form of a
    vCard, 0-2048 bytes"""
