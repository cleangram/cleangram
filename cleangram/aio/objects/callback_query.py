from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...core import CallbackQuery as _CallbackQuery

if TYPE_CHECKING:
    from .message import Message


class CallbackQuery(_CallbackQuery):
    """
    This object represents an incoming callback query from a callback
    button in an inline keyboard. If the button that originated the query
    was attached to a message sent by the bot, the field message will be
    present. If the button was attached to a message sent via the bot (in
    inline mode), the field inline_message_id will be present. Exactly one
    of the fields data or game_short_name will be present.

    Reference: https://core.telegram.org/bots/api#callbackquery
    """

    message: Optional[Message] = None
