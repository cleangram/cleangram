from __future__ import annotations

from .base import TelegramObject


class WebAppInfo(TelegramObject):
    """
    Describes a Web App.

    Reference: https://core.telegram.org/bots/api#webappinfo
    """

    url: str
    """An HTTPS URL of a Web App to be opened with additional data as
    specified in Initializing Web Apps"""
