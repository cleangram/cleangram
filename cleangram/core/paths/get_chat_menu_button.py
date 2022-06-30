from typing import Optional

from ...core.objects.response import Response
from ..objects import MenuButton
from .base import TelegramPath


class GetChatMenuButton(TelegramPath, response=Response[MenuButton]):
    """
    Use this method to get the current value of the bot's menu button in a
    private chat, or the default menu button. Returns MenuButton on
    success.

    Reference: https://core.telegram.org/bots/api#getchatmenubutton
    """

    chat_id: Optional[int] = None
    """Unique identifier for the target private chat. If not specified,
    default bot's menu button will be returned"""
