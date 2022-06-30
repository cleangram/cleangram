from typing import Optional, Union

from ...core.objects.response import Response
from .base import TelegramPath


class PinChatMessage(TelegramPath, response=Response[bool]):
    """
    Use this method to add a message to the list of pinned messages in a
    chat. If the chat is not a private chat, the bot must be an
    administrator in the chat for this to work and must have the
    'can_pin_messages' administrator right in a supergroup or
    'can_edit_messages' administrator right in a channel. Returns True on
    success.

    Reference: https://core.telegram.org/bots/api#pinchatmessage
    """

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target
    channel (in the format @channelusername)"""

    message_id: int
    """Identifier of a message to pin"""

    disable_notification: Optional[bool] = None
    """Pass True, if it is not necessary to send a notification to all chat
    members about the new pinned message. Notifications are always
    disabled in channels and private chats."""
