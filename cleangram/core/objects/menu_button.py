from __future__ import annotations

from .base import TelegramObject


class MenuButton(TelegramObject):
    """
    This object describes the bot's menu button in a private chat. It
    should be one of

        :class:`cleangram.MenuButtonCommands`
        :class:`cleangram.MenuButtonWebApp`
        :class:`cleangram.MenuButtonDefault`
    If a menu button other than MenuButtonDefault is set for a private
    chat, then it is applied in the chat. Otherwise the default menu
    button is applied. By default, the menu button opens the list of bot
    commands.

        :class:`cleangram.MenuButtonCommands`
        :class:`cleangram.MenuButtonWebApp`
        :class:`cleangram.MenuButtonDefault`

    Reference: https://core.telegram.org/bots/api#menubutton
    """
