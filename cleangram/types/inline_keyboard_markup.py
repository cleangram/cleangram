from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .base import TelegramType
from .inline_keyboard_button import InlineKeyboardButton


@dataclass
class InlineKeyboardMarkup(TelegramType):
    """
    This object represents an inline keyboard that appears right
    next to the message it belongs to.
    Reference: https://core.telegram.org/bots/api#inlinekeyboardmarkup
    """

    inline_keyboard: List[List[InlineKeyboardButton]]
    """Array of button rows, each represented by an Array of
    InlineKeyboardButton objects"""
