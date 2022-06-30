from __future__ import annotations

from typing import Optional

from .base import TelegramObject


class SentWebAppMessage(TelegramObject):
    """
    Describes an inline message sent by a Web App on behalf of a user.
    Your bot can accept payments from Telegram users. Please see the
    introduction to payments for more details on the process and how to
    set up payments for your bot. Please note that users will need
    Telegram v.4.0 or higher to use payments (released on May 18, 2017).

    Reference: https://core.telegram.org/bots/api#sentwebappmessage
    """

    inline_message_id: Optional[str] = None
    """Optional. Identifier of the sent inline message. Available only if
    there is an inline keyboard attached to the message."""
