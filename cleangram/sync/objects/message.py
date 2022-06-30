from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union

from ...core import Message as _Message

if TYPE_CHECKING:
    from ...core import (
        ForceReply,
        InlineKeyboardMarkup,
        MessageEntity,
        ReplyKeyboardMarkup,
        ReplyKeyboardRemove,
    )
    from .chat import Chat


class Message(_Message):
    """
    This object represents a message.

    Reference: https://core.telegram.org/bots/api#message
    """

    chat: Chat
    sender_chat: Optional[Chat] = None
    forward_from_chat: Optional[Chat] = None
    reply_to_message: Optional[Message] = None
    pinned_message: Optional[Message] = None

    def answer(
        self,
        text: str,
        parse_mode: Optional[str] = None,
        entities: Optional[List[MessageEntity]] = None,
        disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Union[
            ForceReply,
            ReplyKeyboardRemove,
            None,
            InlineKeyboardMarkup,
            ReplyKeyboardMarkup,
        ] = None,
    ) -> Message:
        return self.bot.send_message(
            chat_id=self.chat.id,
            text=text,
            parse_mode=parse_mode,
            entities=entities,
            disable_web_page_preview=disable_web_page_preview,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup,
        )
