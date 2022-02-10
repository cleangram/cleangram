from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Optional, TYPE_CHECKING, Union

from ..types import Message, Response
from .base import TelegramMethod
from ..utils import fit

if TYPE_CHECKING:
    from ..client import BaseBot


@dataclass
class ForwardMessage(TelegramMethod, response=Response[Message]):
    """
    Use this method to forward messages of any kind. Service
    messages can't be forwarded. On success, the sent Message is
    returned.

    Reference: https://core.telegram.org/bots/api#forwardmessage
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    from_chat_id: Union[str, int]
    """Unique identifier for the chat where the original message
    was sent (or channel username in the format
    @channelusername)"""

    message_id: int
    """Message identifier in the chat specified in from_chat_id"""

    disable_notification: Optional[bool] = field(default=None)
    """Sends the message silently. Users will receive a
    notification with no sound."""

    protect_content: Optional[bool] = field(default=None)
    """Protects the contents of the forwarded message from
    forwarding and saving"""

    def preset(self, bot: BaseBot):
        self.disable_notification = fit(
            self.disable_notification, bot.disable_notification
        )
        self.protect_content = fit(self.protect_content, bot.protect_content)
        return super().preset(bot)
