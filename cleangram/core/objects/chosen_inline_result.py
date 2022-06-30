from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pydantic import Field

from .base import TelegramObject

if TYPE_CHECKING:
    from .location import Location
    from .user import User


class ChosenInlineResult(TelegramObject):
    """
    Represents a result of an inline query that was chosen by the user and
    sent to their chat partner.
    Note: It is necessary to enable inline feedback via @BotFather in
    order to receive these objects in updates.

    Reference: https://core.telegram.org/bots/api#choseninlineresult
    """

    result_id: str
    """The unique identifier for the result that was chosen"""

    from_: User = Field(alias='from')
    """The user that chose the result"""

    query: str
    """The query that was used to obtain the result"""

    location: Optional[Location] = None
    """Optional. Sender location, only for bots that require user location"""

    inline_message_id: Optional[str] = None
    """Optional. Identifier of the sent inline message. Available only if
    there is an inline keyboard attached to the message. Will be also
    received in callback queries and can be used to edit the message."""
