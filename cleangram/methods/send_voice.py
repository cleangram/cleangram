from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union

from ..types import (
    ForceReply,
    InlineKeyboardMarkup,
    InputFile,
    Message,
    MessageEntity,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Response,
)
from .base import TelegramMethod

from ..utils import Presets, attach


@dataclass
class SendVoice(TelegramMethod, response=Response[Message]):
    """
    Use this method to send audio files, if you want Telegram
    clients to display the file as a playable voice message. For
    this to work, your audio must be in an .OGG file encoded
    with OPUS (other formats may be sent as Audio or Document).
    On success, the sent Message is returned. Bots can currently
    send voice messages of up to 50 MB in size, this limit may
    be changed in the future.

    Reference: https://core.telegram.org/bots/api#sendvoice
    """

    chat_id: Union[str, int]
    """Unique identifier for the target chat or username of the
    target channel (in the format @channelusername)"""

    voice: Union[InputFile, str]
    """Audio file to send. Pass a file_id as String to send a file
    that exists on the Telegram servers (recommended), pass an
    HTTP URL as a String for Telegram to get a file from the
    Internet, or upload a new one using multipart/form-data.
    More info on Sending Files »"""

    caption: Optional[str] = field(default=None)
    """Voice message caption, 0-1024 characters after entities
    parsing"""

    parse_mode: Optional[str] = field(default=None)
    """Mode for parsing entities in the voice message caption. See
    formatting options for more details."""

    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """A JSON-serialized list of special entities that appear in
    the caption, which can be specified instead of parse_mode"""

    duration: Optional[int] = field(default=None)
    """Duration of the voice message in seconds"""

    disable_notification: Optional[bool] = field(default=None)
    """Sends the message silently. Users will receive a
    notification with no sound."""

    protect_content: Optional[bool] = field(default=None)
    """Protects the contents of the sent message from forwarding
    and saving"""

    reply_to_message_id: Optional[int] = field(default=None)
    """If the message is a reply, ID of the original message"""

    allow_sending_without_reply: Optional[bool] = field(default=None)
    """Pass True, if the message should be sent even if the
    specified replied-to message is not found"""

    reply_markup: Optional[
        Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ]
    ] = field(default=None)
    """Additional interface options. A JSON-serialized object for
    an inline keyboard, custom reply keyboard, instructions to
    remove reply keyboard or to force a reply from the user."""

    def preset(self, presets: Presets) -> Dict[str, InputFile]:
        presets.parse_mode(self)
        presets.disable_notification(self)
        presets.protect_content(self)
        presets.allow_sending_without_reply(self)
        files = super(SendVoice, self).preset(presets)
        self.voice = attach(self.voice, files)
        return files
