from __future__ import annotations

from .passport_element_error import PassportElementError


class PassportElementErrorUnspecified(PassportElementError):
    """
    Represents an issue in an unspecified place. The error is considered
    resolved when new data is added.
    Your bot can offer users HTML5 games to play solo or to compete
    against each other in groups and one-on-one chats. Create games via
    @BotFather using the /newgame command. Please note that this kind of
    power requires responsibility: you will need to accept the terms for
    each game that your bots will be offering.

    Reference: https://core.telegram.org/bots/api#passportelementerrorunspecified
    """

    type: str
    """Type of element of the user's Telegram Passport which has the issue"""

    element_hash: str
    """Base64-encoded element hash"""

    message: str
    """Error message"""

    source: str = 'unspecified'
    """Error source, must be unspecified"""
