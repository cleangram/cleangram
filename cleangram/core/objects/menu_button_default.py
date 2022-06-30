from __future__ import annotations

from .menu_button import MenuButton


class MenuButtonDefault(MenuButton):
    """
    Describes that no specific value for the menu button was set.

    Reference: https://core.telegram.org/bots/api#menubuttondefault
    """

    type: str = 'default'
    """Type of the button, must be default"""
