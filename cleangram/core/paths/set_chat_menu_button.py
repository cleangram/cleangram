from typing import Optional

from ...core.objects.response import Response
from ..objects import MenuButton
from .base import TelegramPath


class SetChatMenuButton(TelegramPath, response=Response[bool]):
    """
    Use this method to change the bot's menu button in a private chat, or
    the default menu button. Returns True on success.

    Reference: https://core.telegram.org/bots/api#setchatmenubutton
    """

    chat_id: Optional[int] = None
    """Unique identifier for the target private chat. If not specified,
    default bot's menu button will be changed"""

    menu_button: Optional[MenuButton] = None
    """A JSON-serialized object for the bot's new menu button. Defaults to
    MenuButtonDefault"""
