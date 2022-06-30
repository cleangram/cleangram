from .animation import Animation
from .audio import Audio
from .base import TelegramObject
from .bot_command import BotCommand
from .bot_command_scope import BotCommandScope
from .bot_command_scope_all_chat_administrators import (
    BotCommandScopeAllChatAdministrators,
)
from .bot_command_scope_all_group_chats import BotCommandScopeAllGroupChats
from .bot_command_scope_all_private_chats import BotCommandScopeAllPrivateChats
from .bot_command_scope_chat import BotCommandScopeChat
from .bot_command_scope_chat_administrators import (
    BotCommandScopeChatAdministrators,
)
from .bot_command_scope_chat_member import BotCommandScopeChatMember
from .bot_command_scope_default import BotCommandScopeDefault
from .callback_game import CallbackGame
from .callback_query import CallbackQuery
from .chat import Chat
from .chat_administrator_rights import ChatAdministratorRights
from .chat_invite_link import ChatInviteLink
from .chat_join_request import ChatJoinRequest
from .chat_location import ChatLocation
from .chat_member import ChatMember
from .chat_member_administrator import ChatMemberAdministrator
from .chat_member_banned import ChatMemberBanned
from .chat_member_left import ChatMemberLeft
from .chat_member_member import ChatMemberMember
from .chat_member_owner import ChatMemberOwner
from .chat_member_restricted import ChatMemberRestricted
from .chat_member_updated import ChatMemberUpdated
from .chat_permissions import ChatPermissions
from .chat_photo import ChatPhoto
from .chosen_inline_result import ChosenInlineResult
from .contact import Contact
from .dice import Dice
from .document import Document
from .encrypted_credentials import EncryptedCredentials
from .encrypted_passport_element import EncryptedPassportElement
from .file import File
from .force_reply import ForceReply
from .game import Game
from .game_high_score import GameHighScore
from .inline_keyboard_button import InlineKeyboardButton
from .inline_keyboard_markup import InlineKeyboardMarkup
from .inline_query import InlineQuery
from .inline_query_result import InlineQueryResult
from .inline_query_result_article import InlineQueryResultArticle
from .inline_query_result_audio import InlineQueryResultAudio
from .inline_query_result_cached_audio import InlineQueryResultCachedAudio
from .inline_query_result_cached_document import (
    InlineQueryResultCachedDocument,
)
from .inline_query_result_cached_gif import InlineQueryResultCachedGif
from .inline_query_result_cached_mpeg_4_gif import (
    InlineQueryResultCachedMpeg4Gif,
)
from .inline_query_result_cached_photo import InlineQueryResultCachedPhoto
from .inline_query_result_cached_sticker import InlineQueryResultCachedSticker
from .inline_query_result_cached_video import InlineQueryResultCachedVideo
from .inline_query_result_cached_voice import InlineQueryResultCachedVoice
from .inline_query_result_contact import InlineQueryResultContact
from .inline_query_result_document import InlineQueryResultDocument
from .inline_query_result_game import InlineQueryResultGame
from .inline_query_result_gif import InlineQueryResultGif
from .inline_query_result_location import InlineQueryResultLocation
from .inline_query_result_mpeg_4_gif import InlineQueryResultMpeg4Gif
from .inline_query_result_photo import InlineQueryResultPhoto
from .inline_query_result_venue import InlineQueryResultVenue
from .inline_query_result_video import InlineQueryResultVideo
from .inline_query_result_voice import InlineQueryResultVoice
from .input_contact_message_content import InputContactMessageContent
from .input_file import InputFile
from .input_invoice_message_content import InputInvoiceMessageContent
from .input_location_message_content import InputLocationMessageContent
from .input_media import InputMedia
from .input_media_animation import InputMediaAnimation
from .input_media_audio import InputMediaAudio
from .input_media_document import InputMediaDocument
from .input_media_photo import InputMediaPhoto
from .input_media_video import InputMediaVideo
from .input_message_content import InputMessageContent
from .input_text_message_content import InputTextMessageContent
from .input_venue_message_content import InputVenueMessageContent
from .invoice import Invoice
from .keyboard_button import KeyboardButton
from .keyboard_button_poll_type import KeyboardButtonPollType
from .labeled_price import LabeledPrice
from .location import Location
from .login_url import LoginUrl
from .mask_position import MaskPosition
from .menu_button import MenuButton
from .menu_button_commands import MenuButtonCommands
from .menu_button_default import MenuButtonDefault
from .menu_button_web_app import MenuButtonWebApp
from .message import Message
from .message_auto_delete_timer_changed import MessageAutoDeleteTimerChanged
from .message_entity import MessageEntity
from .message_id import MessageId
from .order_info import OrderInfo
from .passport_data import PassportData
from .passport_element_error import PassportElementError
from .passport_element_error_data_field import PassportElementErrorDataField
from .passport_element_error_file import PassportElementErrorFile
from .passport_element_error_files import PassportElementErrorFiles
from .passport_element_error_front_side import PassportElementErrorFrontSide
from .passport_element_error_reverse_side import (
    PassportElementErrorReverseSide,
)
from .passport_element_error_selfie import PassportElementErrorSelfie
from .passport_element_error_translation_file import (
    PassportElementErrorTranslationFile,
)
from .passport_element_error_translation_files import (
    PassportElementErrorTranslationFiles,
)
from .passport_element_error_unspecified import PassportElementErrorUnspecified
from .passport_file import PassportFile
from .photo_size import PhotoSize
from .poll import Poll
from .poll_answer import PollAnswer
from .poll_option import PollOption
from .pre_checkout_query import PreCheckoutQuery
from .proximity_alert_triggered import ProximityAlertTriggered
from .reply_keyboard_markup import ReplyKeyboardMarkup
from .reply_keyboard_remove import ReplyKeyboardRemove
from .request import Request
from .response import Response, T
from .response_parameters import ResponseParameters
from .sent_web_app_message import SentWebAppMessage
from .shipping_address import ShippingAddress
from .shipping_option import ShippingOption
from .shipping_query import ShippingQuery
from .sticker import Sticker
from .sticker_set import StickerSet
from .successful_payment import SuccessfulPayment
from .update import Update
from .user import User
from .user_profile_photos import UserProfilePhotos
from .venue import Venue
from .video import Video
from .video_chat_ended import VideoChatEnded
from .video_chat_participants_invited import VideoChatParticipantsInvited
from .video_chat_scheduled import VideoChatScheduled
from .video_chat_started import VideoChatStarted
from .video_note import VideoNote
from .voice import Voice
from .web_app_data import WebAppData
from .web_app_info import WebAppInfo
from .webhook_info import WebhookInfo

__all__ = [
    'Animation',
    'Audio',
    'BotCommand',
    'BotCommandScope',
    'BotCommandScopeAllChatAdministrators',
    'BotCommandScopeAllGroupChats',
    'BotCommandScopeAllPrivateChats',
    'BotCommandScopeChat',
    'BotCommandScopeChatAdministrators',
    'BotCommandScopeChatMember',
    'BotCommandScopeDefault',
    'CallbackGame',
    'CallbackQuery',
    'Chat',
    'ChatAdministratorRights',
    'ChatInviteLink',
    'ChatJoinRequest',
    'ChatLocation',
    'ChatMember',
    'ChatMemberAdministrator',
    'ChatMemberBanned',
    'ChatMemberLeft',
    'ChatMemberMember',
    'ChatMemberOwner',
    'ChatMemberRestricted',
    'ChatMemberUpdated',
    'ChatPermissions',
    'ChatPhoto',
    'ChosenInlineResult',
    'Contact',
    'Dice',
    'Document',
    'EncryptedCredentials',
    'EncryptedPassportElement',
    'File',
    'ForceReply',
    'Game',
    'GameHighScore',
    'InlineKeyboardButton',
    'InlineKeyboardMarkup',
    'InlineQuery',
    'InlineQueryResult',
    'InlineQueryResultArticle',
    'InlineQueryResultAudio',
    'InlineQueryResultCachedAudio',
    'InlineQueryResultCachedDocument',
    'InlineQueryResultCachedGif',
    'InlineQueryResultCachedMpeg4Gif',
    'InlineQueryResultCachedPhoto',
    'InlineQueryResultCachedSticker',
    'InlineQueryResultCachedVideo',
    'InlineQueryResultCachedVoice',
    'InlineQueryResultContact',
    'InlineQueryResultDocument',
    'InlineQueryResultGame',
    'InlineQueryResultGif',
    'InlineQueryResultLocation',
    'InlineQueryResultMpeg4Gif',
    'InlineQueryResultPhoto',
    'InlineQueryResultVenue',
    'InlineQueryResultVideo',
    'InlineQueryResultVoice',
    'InputContactMessageContent',
    'InputFile',
    'InputInvoiceMessageContent',
    'InputLocationMessageContent',
    'InputMedia',
    'InputMediaAnimation',
    'InputMediaAudio',
    'InputMediaDocument',
    'InputMediaPhoto',
    'InputMediaVideo',
    'InputMessageContent',
    'InputTextMessageContent',
    'InputVenueMessageContent',
    'Invoice',
    'KeyboardButton',
    'KeyboardButtonPollType',
    'LabeledPrice',
    'Location',
    'LoginUrl',
    'MaskPosition',
    'MenuButton',
    'MenuButtonCommands',
    'MenuButtonDefault',
    'MenuButtonWebApp',
    'Message',
    'MessageAutoDeleteTimerChanged',
    'MessageEntity',
    'MessageId',
    'OrderInfo',
    'PassportData',
    'PassportElementError',
    'PassportElementErrorDataField',
    'PassportElementErrorFile',
    'PassportElementErrorFiles',
    'PassportElementErrorFrontSide',
    'PassportElementErrorReverseSide',
    'PassportElementErrorSelfie',
    'PassportElementErrorTranslationFile',
    'PassportElementErrorTranslationFiles',
    'PassportElementErrorUnspecified',
    'PassportFile',
    'PhotoSize',
    'Poll',
    'PollAnswer',
    'PollOption',
    'PreCheckoutQuery',
    'ProximityAlertTriggered',
    'ReplyKeyboardMarkup',
    'ReplyKeyboardRemove',
    'Request',
    'Response',
    'ResponseParameters',
    'SentWebAppMessage',
    'ShippingAddress',
    'ShippingOption',
    'ShippingQuery',
    'Sticker',
    'StickerSet',
    'SuccessfulPayment',
    'T',
    'TelegramObject',
    'Update',
    'User',
    'UserProfilePhotos',
    'Venue',
    'Video',
    'VideoChatEnded',
    'VideoChatParticipantsInvited',
    'VideoChatScheduled',
    'VideoChatStarted',
    'VideoNote',
    'Voice',
    'WebAppData',
    'WebAppInfo',
    'WebhookInfo',
]
Update.update_forward_refs(
    Poll=Poll,
    PreCheckoutQuery=PreCheckoutQuery,
    PollAnswer=PollAnswer,
    ChosenInlineResult=ChosenInlineResult,
    CallbackQuery=CallbackQuery,
    ChatJoinRequest=ChatJoinRequest,
    Message=Message,
    ChatMemberUpdated=ChatMemberUpdated,
    ShippingQuery=ShippingQuery,
    InlineQuery=InlineQuery,
)
Chat.update_forward_refs(
    ChatPermissions=ChatPermissions,
    ChatPhoto=ChatPhoto,
    Message=Message,
    ChatLocation=ChatLocation,
)
Message.update_forward_refs(
    Invoice=Invoice,
    SuccessfulPayment=SuccessfulPayment,
    PassportData=PassportData,
    VideoNote=VideoNote,
    WebAppData=WebAppData,
    Document=Document,
    Location=Location,
    Dice=Dice,
    Chat=Chat,
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    MessageAutoDeleteTimerChanged=MessageAutoDeleteTimerChanged,
    ProximityAlertTriggered=ProximityAlertTriggered,
    Audio=Audio,
    PhotoSize=PhotoSize,
    Contact=Contact,
    VideoChatStarted=VideoChatStarted,
    VideoChatScheduled=VideoChatScheduled,
    Game=Game,
    Poll=Poll,
    VideoChatParticipantsInvited=VideoChatParticipantsInvited,
    Animation=Animation,
    Sticker=Sticker,
    MessageEntity=MessageEntity,
    VideoChatEnded=VideoChatEnded,
    Video=Video,
    Voice=Voice,
    User=User,
    Venue=Venue,
)
MessageEntity.update_forward_refs(User=User)
Animation.update_forward_refs(PhotoSize=PhotoSize)
Audio.update_forward_refs(PhotoSize=PhotoSize)
Document.update_forward_refs(PhotoSize=PhotoSize)
Video.update_forward_refs(PhotoSize=PhotoSize)
VideoNote.update_forward_refs(PhotoSize=PhotoSize)
PollAnswer.update_forward_refs(User=User)
Poll.update_forward_refs(PollOption=PollOption, MessageEntity=MessageEntity)
Venue.update_forward_refs(Location=Location)
ProximityAlertTriggered.update_forward_refs(User=User)
VideoChatParticipantsInvited.update_forward_refs(User=User)
UserProfilePhotos.update_forward_refs(PhotoSize=PhotoSize)
ReplyKeyboardMarkup.update_forward_refs(KeyboardButton=KeyboardButton)
KeyboardButton.update_forward_refs(
    WebAppInfo=WebAppInfo, KeyboardButtonPollType=KeyboardButtonPollType
)
InlineKeyboardMarkup.update_forward_refs(
    InlineKeyboardButton=InlineKeyboardButton
)
InlineKeyboardButton.update_forward_refs(
    LoginUrl=LoginUrl, WebAppInfo=WebAppInfo, CallbackGame=CallbackGame
)
CallbackQuery.update_forward_refs(User=User, Message=Message)
ChatInviteLink.update_forward_refs(User=User)
ChatMemberOwner.update_forward_refs(User=User)
ChatMemberAdministrator.update_forward_refs(User=User)
ChatMemberMember.update_forward_refs(User=User)
ChatMemberRestricted.update_forward_refs(User=User)
ChatMemberLeft.update_forward_refs(User=User)
ChatMemberBanned.update_forward_refs(User=User)
ChatMemberUpdated.update_forward_refs(
    ChatInviteLink=ChatInviteLink, Chat=Chat, User=User, ChatMember=ChatMember
)
ChatJoinRequest.update_forward_refs(
    ChatInviteLink=ChatInviteLink, Chat=Chat, User=User
)
ChatLocation.update_forward_refs(Location=Location)
MenuButtonWebApp.update_forward_refs(WebAppInfo=WebAppInfo)
InputMediaPhoto.update_forward_refs(
    InputFile=InputFile, MessageEntity=MessageEntity
)
InputMediaVideo.update_forward_refs(
    InputFile=InputFile, MessageEntity=MessageEntity
)
InputMediaAnimation.update_forward_refs(
    InputFile=InputFile, MessageEntity=MessageEntity
)
InputMediaAudio.update_forward_refs(
    InputFile=InputFile, MessageEntity=MessageEntity
)
InputMediaDocument.update_forward_refs(
    InputFile=InputFile, MessageEntity=MessageEntity
)
Sticker.update_forward_refs(
    PhotoSize=PhotoSize, MaskPosition=MaskPosition, File=File
)
StickerSet.update_forward_refs(PhotoSize=PhotoSize, Sticker=Sticker)
InlineQuery.update_forward_refs(User=User, Location=Location)
InlineQueryResultArticle.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
)
InlineQueryResultPhoto.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
    MessageEntity=MessageEntity,
)
InlineQueryResultGif.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
    MessageEntity=MessageEntity,
)
InlineQueryResultMpeg4Gif.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
    MessageEntity=MessageEntity,
)
InlineQueryResultVideo.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
    MessageEntity=MessageEntity,
)
InlineQueryResultAudio.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
    MessageEntity=MessageEntity,
)
InlineQueryResultVoice.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
    MessageEntity=MessageEntity,
)
InlineQueryResultDocument.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
    MessageEntity=MessageEntity,
)
InlineQueryResultLocation.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
)
InlineQueryResultVenue.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
)
InlineQueryResultContact.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
)
InlineQueryResultGame.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup
)
InlineQueryResultCachedPhoto.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
    MessageEntity=MessageEntity,
)
InlineQueryResultCachedGif.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
    MessageEntity=MessageEntity,
)
InlineQueryResultCachedMpeg4Gif.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
    MessageEntity=MessageEntity,
)
InlineQueryResultCachedSticker.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
)
InlineQueryResultCachedDocument.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
    MessageEntity=MessageEntity,
)
InlineQueryResultCachedVideo.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
    MessageEntity=MessageEntity,
)
InlineQueryResultCachedVoice.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
    MessageEntity=MessageEntity,
)
InlineQueryResultCachedAudio.update_forward_refs(
    InlineKeyboardMarkup=InlineKeyboardMarkup,
    InputMessageContent=InputMessageContent,
    MessageEntity=MessageEntity,
)
InputTextMessageContent.update_forward_refs(MessageEntity=MessageEntity)
InputInvoiceMessageContent.update_forward_refs(LabeledPrice=LabeledPrice)
ChosenInlineResult.update_forward_refs(User=User, Location=Location)
OrderInfo.update_forward_refs(ShippingAddress=ShippingAddress)
ShippingOption.update_forward_refs(LabeledPrice=LabeledPrice)
SuccessfulPayment.update_forward_refs(OrderInfo=OrderInfo)
ShippingQuery.update_forward_refs(ShippingAddress=ShippingAddress, User=User)
PreCheckoutQuery.update_forward_refs(User=User, OrderInfo=OrderInfo)
PassportData.update_forward_refs(
    EncryptedPassportElement=EncryptedPassportElement,
    EncryptedCredentials=EncryptedCredentials,
)
EncryptedPassportElement.update_forward_refs(PassportFile=PassportFile)
Game.update_forward_refs(
    PhotoSize=PhotoSize, Animation=Animation, MessageEntity=MessageEntity
)
GameHighScore.update_forward_refs(User=User)
