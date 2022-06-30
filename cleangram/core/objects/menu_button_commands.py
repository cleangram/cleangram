from __future__ import annotations

from .menu_button import MenuButton


class MenuButtonCommands(MenuButton):
    """
    Represents a menu button, which opens the bot's list of commands.

    Reference: https://core.telegram.org/bots/api#menubuttoncommands
    """

    type: str = 'commands'
    """Type of the button, must be commands"""
