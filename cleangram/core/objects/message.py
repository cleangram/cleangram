from __future__ import annotations

import abc
from typing import TYPE_CHECKING, List, Optional

from pydantic import Field

from ..bot.bot import Bot
from .base import TelegramObject

if TYPE_CHECKING:
    from .animation import Animation
    from .audio import Audio
    from .chat import Chat
    from .contact import Contact
    from .dice import Dice
    from .document import Document
    from .game import Game
    from .inline_keyboard_markup import InlineKeyboardMarkup
    from .invoice import Invoice
    from .location import Location
    from .message_auto_delete_timer_changed import (
        MessageAutoDeleteTimerChanged,
    )
    from .message_entity import MessageEntity
    from .passport_data import PassportData
    from .photo_size import PhotoSize
    from .poll import Poll
    from .proximity_alert_triggered import ProximityAlertTriggered
    from .sticker import Sticker
    from .successful_payment import SuccessfulPayment
    from .user import User
    from .venue import Venue
    from .video import Video
    from .video_chat_ended import VideoChatEnded
    from .video_chat_participants_invited import VideoChatParticipantsInvited
    from .video_chat_scheduled import VideoChatScheduled
    from .video_chat_started import VideoChatStarted
    from .video_note import VideoNote
    from .voice import Voice
    from .web_app_data import WebAppData


class Message(TelegramObject, abc.ABC):
    """
    This object represents a message.

    Reference: https://core.telegram.org/bots/api#message
    """

    message_id: int
    """Unique message identifier inside this chat"""

    date: int
    """Date the message was sent in Unix time"""

    chat: Chat
    """Conversation the message belongs to"""

    from_: Optional[User] = Field(alias='from')
    """Optional. Sender of the message; empty for messages sent to channels.
    For backward compatibility, the field contains a fake sender user in
    non-channel chats, if the message was sent on behalf of a chat."""

    sender_chat: Optional[Chat] = None
    """Optional. Sender of the message, sent on behalf of a chat. For
    example, the channel itself for channel posts, the supergroup itself
    for messages from anonymous group administrators, the linked channel
    for messages automatically forwarded to the discussion group. For
    backward compatibility, the field from contains a fake sender user in
    non-channel chats, if the message was sent on behalf of a chat."""

    forward_from: Optional[User] = None
    """Optional. For forwarded messages, sender of the original message"""

    forward_from_chat: Optional[Chat] = None
    """Optional. For messages forwarded from channels or from anonymous
    administrators, information about the original sender chat"""

    forward_from_message_id: Optional[int] = None
    """Optional. For messages forwarded from channels, identifier of the
    original message in the channel"""

    forward_signature: Optional[str] = None
    """Optional. For forwarded messages that were originally sent in channels
    or by an anonymous chat administrator, signature of the message sender
    if present"""

    forward_sender_name: Optional[str] = None
    """Optional. Sender's name for messages forwarded from users who disallow
    adding a link to their account in forwarded messages"""

    forward_date: Optional[int] = None
    """Optional. For forwarded messages, date the original message was sent
    in Unix time"""

    is_automatic_forward: Optional[bool] = None
    """Optional. True, if the message is a channel post that was
    automatically forwarded to the connected discussion group"""

    reply_to_message: Optional[Message] = None
    """Optional. For replies, the original message. Note that the Message
    object in this field will not contain further reply_to_message fields
    even if it itself is a reply."""

    via_bot: Optional[User] = None
    """Optional. Bot through which the message was sent"""

    edit_date: Optional[int] = None
    """Optional. Date the message was last edited in Unix time"""

    has_protected_content: Optional[bool] = None
    """Optional. True, if the message can't be forwarded"""

    media_group_id: Optional[str] = None
    """Optional. The unique identifier of a media message group this message
    belongs to"""

    author_signature: Optional[str] = None
    """Optional. Signature of the post author for messages in channels, or
    the custom title of an anonymous group administrator"""

    text: Optional[str] = None
    """Optional. For text messages, the actual UTF-8 text of the message"""

    entities: Optional[List[MessageEntity]] = Field(default_factory=list)
    """Optional. For text messages, special entities like usernames, URLs,
    bot commands, etc. that appear in the text"""

    animation: Optional[Animation] = None
    """Optional. Message is an animation, information about the animation.
    For backward compatibility, when this field is set, the document field
    will also be set"""

    audio: Optional[Audio] = None
    """Optional. Message is an audio file, information about the file"""

    document: Optional[Document] = None
    """Optional. Message is a general file, information about the file"""

    photo: Optional[List[PhotoSize]] = Field(default_factory=list)
    """Optional. Message is a photo, available sizes of the photo"""

    sticker: Optional[Sticker] = None
    """Optional. Message is a sticker, information about the sticker"""

    video: Optional[Video] = None
    """Optional. Message is a video, information about the video"""

    video_note: Optional[VideoNote] = None
    """Optional. Message is a video note, information about the video message"""

    voice: Optional[Voice] = None
    """Optional. Message is a voice message, information about the file"""

    caption: Optional[str] = None
    """Optional. Caption for the animation, audio, document, photo, video or
    voice"""

    caption_entities: Optional[List[MessageEntity]] = Field(
        default_factory=list
    )
    """Optional. For messages with a caption, special entities like
    usernames, URLs, bot commands, etc. that appear in the caption"""

    contact: Optional[Contact] = None
    """Optional. Message is a shared contact, information about the contact"""

    dice: Optional[Dice] = None
    """Optional. Message is a dice with random value"""

    game: Optional[Game] = None
    """Optional. Message is a game, information about the game. More about
    games »"""

    poll: Optional[Poll] = None
    """Optional. Message is a native poll, information about the poll"""

    venue: Optional[Venue] = None
    """Optional. Message is a venue, information about the venue. For
    backward compatibility, when this field is set, the location field
    will also be set"""

    location: Optional[Location] = None
    """Optional. Message is a shared location, information about the location"""

    new_chat_members: Optional[List[User]] = Field(default_factory=list)
    """Optional. New members that were added to the group or supergroup and
    information about them (the bot itself may be one of these members)"""

    left_chat_member: Optional[User] = None
    """Optional. A member was removed from the group, information about them
    (this member may be the bot itself)"""

    new_chat_title: Optional[str] = None
    """Optional. A chat title was changed to this value"""

    new_chat_photo: Optional[List[PhotoSize]] = Field(default_factory=list)
    """Optional. A chat photo was change to this value"""

    delete_chat_photo: Optional[bool] = None
    """Optional. Service message: the chat photo was deleted"""

    group_chat_created: Optional[bool] = None
    """Optional. Service message: the group has been created"""

    supergroup_chat_created: Optional[bool] = None
    """Optional. Service message: the supergroup has been created. This field
    can't be received in a message coming through updates, because bot
    can't be a member of a supergroup when it is created. It can only be
    found in reply_to_message if someone replies to a very first message
    in a directly created supergroup."""

    channel_chat_created: Optional[bool] = None
    """Optional. Service message: the channel has been created. This field
    can't be received in a message coming through updates, because bot
    can't be a member of a channel when it is created. It can only be
    found in reply_to_message if someone replies to a very first message
    in a channel."""

    message_auto_delete_timer_changed: Optional[
        MessageAutoDeleteTimerChanged
    ] = None
    """Optional. Service message: auto-delete timer settings changed in the
    chat"""

    migrate_to_chat_id: Optional[int] = None
    """Optional. The group has been migrated to a supergroup with the
    specified identifier. This number may have more than 32 significant
    bits and some programming languages may have difficulty/silent defects
    in interpreting it. But it has at most 52 significant bits, so a
    signed 64-bit integer or double-precision float type are safe for
    storing this identifier."""

    migrate_from_chat_id: Optional[int] = None
    """Optional. The supergroup has been migrated from a group with the
    specified identifier. This number may have more than 32 significant
    bits and some programming languages may have difficulty/silent defects
    in interpreting it. But it has at most 52 significant bits, so a
    signed 64-bit integer or double-precision float type are safe for
    storing this identifier."""

    pinned_message: Optional[Message] = None
    """Optional. Specified message was pinned. Note that the Message object
    in this field will not contain further reply_to_message fields even if
    it is itself a reply."""

    invoice: Optional[Invoice] = None
    """Optional. Message is an invoice for a payment, information about the
    invoice. More about payments »"""

    successful_payment: Optional[SuccessfulPayment] = None
    """Optional. Message is a service message about a successful payment,
    information about the payment. More about payments »"""

    connected_website: Optional[str] = None
    """Optional. The domain name of the website on which the user has logged
    in. More about Telegram Login »"""

    passport_data: Optional[PassportData] = None
    """Optional. Telegram Passport data"""

    proximity_alert_triggered: Optional[ProximityAlertTriggered] = None
    """Optional. Service message. A user in the chat triggered another user's
    proximity alert while sharing Live Location."""

    video_chat_scheduled: Optional[VideoChatScheduled] = None
    """Optional. Service message: video chat scheduled"""

    video_chat_started: Optional[VideoChatStarted] = None
    """Optional. Service message: video chat started"""

    video_chat_ended: Optional[VideoChatEnded] = None
    """Optional. Service message: video chat ended"""

    video_chat_participants_invited: Optional[
        VideoChatParticipantsInvited
    ] = None
    """Optional. Service message: new participants invited to a video chat"""

    web_app_data: Optional[WebAppData] = None
    """Optional. Service message: data sent by a Web App"""

    reply_markup: Optional[InlineKeyboardMarkup] = None
    """Optional. Inline keyboard attached to the message. login_url buttons
    are represented as ordinary url buttons."""

    @abc.abstractmethod
    def answer(
        self,
        text,
        parse_mode=None,
        entities=None,
        disable_web_page_preview=None,
        disable_notification=None,
        protect_content=None,
        reply_to_message_id=None,
        allow_sending_without_reply=None,
        reply_markup=None,
    ):
        ...

    def adjust(self, bot: Bot):
        self.chat.adjust(bot)
        if self.sender_chat:
            self.sender_chat.adjust(bot)
        if self.forward_from_chat:
            self.forward_from_chat.adjust(bot)
        if self.reply_to_message:
            self.reply_to_message.adjust(bot)
        if self.pinned_message:
            self.pinned_message.adjust(bot)
