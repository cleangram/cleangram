from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, TYPE_CHECKING, Union

from ..types import InputFile, Response
from .base import TelegramMethod
from ..utils import attach
from ..utils import fit

if TYPE_CHECKING:
    from ..client import BaseBot


@dataclass
class SetChatPhoto(TelegramMethod, response=Response[bool]):
    """
    Use this method to set a new profile photo for the chat.
    Photos can't be changed for private chats. The bot must be
    an administrator in the chat for this to work and must have
    the appropriate administrator rights. Returns True on
    success.

    Reference: https://core.telegram.org/bots/api#setchatphoto
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    photo: InputFile
    """New chat photo, uploaded using multipart/form-data"""

    def preset(self, bot: BaseBot) -> Dict[str, InputFile]:
        files = super().preset(bot)
        self.photo = attach(self.photo, files)
        return files
