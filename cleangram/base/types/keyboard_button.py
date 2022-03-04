from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .base import TelegramType
from .keyboard_button_poll_type import KeyboardButtonPollType


@dataclass
class KeyboardButton(TelegramType):
    """
    This object represents one button of the reply keyboard. For
    simple text buttons String can be used instead of this
    object to specify text of the button. Optional fields
    request_contact, request_location, and request_poll are
    mutually exclusive.
    Reference: https://core.telegram.org/bots/api#keyboardbutton
    """

    text: str
    """Text of the button. If none of the optional fields are used,
    it will be sent as a message when the button is pressed"""

    request_contact: Optional[bool] = field(default=None)
    """Optional. If True, the user's phone number will be sent as a
    contact when the button is pressed. Available in private
    chats only"""

    request_location: Optional[bool] = field(default=None)
    """Optional. If True, the user's current location will be sent
    when the button is pressed. Available in private chats only"""

    request_poll: Optional[KeyboardButtonPollType] = field(default=None)
    """Optional. If specified, the user will be asked to create a
    poll and send it to the bot when the button is pressed.
    Available in private chats only"""
