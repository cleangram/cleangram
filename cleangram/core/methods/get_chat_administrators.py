from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union

from ..types import (
    Response,
    ChatMember
)
from .base import TelegramMethod


@dataclass
class GetChatAdministrators(TelegramMethod, response=Response[List[ChatMember]]):
    """
    Use this method to get a list of administrators in a chat.
    On success, returns an Array of ChatMember objects that
    contains information about all chat administrators except
    other bots. If the chat is a group or a supergroup and no
    administrators were appointed, only the creator will be
    returned.

    Reference: https://core.telegram.org/bots/api#getchatadministrators
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target supergroup or channel (in the format
    @channelusername)"""
