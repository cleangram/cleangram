from __future__ import annotations

from typing import Optional, List, Union


from ..types import (
    BotCommand,
    BotCommandScope,
    ChatInfo,
    ChatInviteLink,
    ChatMember,
    ChatPermissions,
    File,
    ForceReply,
    GameHighScore,
    InlineKeyboardMarkup,
    InlineQueryResult,
    InputFile,
    InputMedia,
    InputMediaAudio,
    InputMediaDocument,
    InputMediaPhoto,
    InputMediaVideo,
    LabeledPrice,
    MaskPosition,
    Message,
    MessageEntity,
    MessageId,
    PassportElementError,
    Poll,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ShippingOption,
    StickerSet,
    Update,
    User,
    UserProfilePhotos,
    WebhookInfo
)
from ..methods import (
    AddStickerToSet,
    AnswerCallbackQuery,
    AnswerInlineQuery,
    AnswerPreCheckoutQuery,
    AnswerShippingQuery,
    ApproveChatJoinRequest,
    BanChatMember,
    BanChatSenderChat,
    Close,
    CopyMessage,
    CreateChatInviteLink,
    CreateNewStickerSet,
    DeclineChatJoinRequest,
    DeleteChatPhoto,
    DeleteChatStickerSet,
    DeleteMessage,
    DeleteMyCommands,
    DeleteStickerFromSet,
    DeleteWebhook,
    EditChatInviteLink,
    EditMessageCaption,
    EditMessageLiveLocation,
    EditMessageMedia,
    EditMessageReplyMarkup,
    EditMessageText,
    ExportChatInviteLink,
    ForwardMessage,
    GetChat,
    GetChatAdministrators,
    GetChatMember,
    GetChatMemberCount,
    GetFile,
    GetGameHighScores,
    GetMe,
    GetMyCommands,
    GetStickerSet,
    GetUpdates,
    GetUserProfilePhotos,
    GetWebhookInfo,
    LeaveChat,
    LogOut,
    PinChatMessage,
    PromoteChatMember,
    RestrictChatMember,
    RevokeChatInviteLink,
    SendAnimation,
    SendAudio,
    SendChatAction,
    SendContact,
    SendDice,
    SendDocument,
    SendGame,
    SendInvoice,
    SendLocation,
    SendMediaGroup,
    SendMessage,
    SendPhoto,
    SendPoll,
    SendSticker,
    SendVenue,
    SendVideo,
    SendVideoNote,
    SendVoice,
    SetChatAdministratorCustomTitle,
    SetChatDescription,
    SetChatPermissions,
    SetChatPhoto,
    SetChatStickerSet,
    SetChatTitle,
    SetGameScore,
    SetMyCommands,
    SetPassportDataErrors,
    SetStickerPositionInSet,
    SetStickerSetThumb,
    SetWebhook,
    StopMessageLiveLocation,
    StopPoll,
    UnbanChatMember,
    UnbanChatSenderChat,
    UnpinAllChatMessages,
    UnpinChatMessage,
    UploadStickerFile
)
from .base import BaseBot


class Bot(BaseBot):
    """
    Bot client for work with Telegram Bot API
    """
    async def get_updates(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        allowed_updates: Optional[List[str]] = None
    ) -> List[Update]:
        return await self(GetUpdates(
            offset=offset,
            limit=limit,
            timeout=timeout,
            allowed_updates=allowed_updates
        ))

    async def set_webhook(
        self,
        url: str,
        certificate: Optional[InputFile] = None,
        ip_address: Optional[str] = None,
        max_connections: Optional[int] = None,
        allowed_updates: Optional[List[str]] = None,
        drop_pending_updates: Optional[bool] = None
    ) -> bool:
        return await self(SetWebhook(
            url=url,
            certificate=certificate,
            ip_address=ip_address,
            max_connections=max_connections,
            allowed_updates=allowed_updates,
            drop_pending_updates=drop_pending_updates
        ))

    async def delete_webhook(
        self,
        drop_pending_updates: Optional[bool] = None
    ) -> bool:
        return await self(DeleteWebhook(
            drop_pending_updates=drop_pending_updates
        ))

    async def get_webhook_info(
        self,
    ) -> WebhookInfo:
        return await self(GetWebhookInfo())

    async def get_me(
        self,
    ) -> User:
        return await self(GetMe())

    async def log_out(
        self,
    ) -> bool:
        return await self(LogOut())

    async def close(
        self,
    ) -> bool:
        return await self(Close())

    async def send_message(
        self,
        chat_id: Union[str, int],
        text: str,
        parse_mode: Optional[str] = None,
        entities: Optional[List[MessageEntity]] = None,
        disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        return await self(SendMessage(
            chat_id=chat_id,
            text=text,
            parse_mode=parse_mode,
            entities=entities,
            disable_web_page_preview=disable_web_page_preview,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def forward_message(
        self,
        chat_id: Union[str, int],
        from_chat_id: Union[str, int],
        message_id: int,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None
    ) -> Message:
        return await self(ForwardMessage(
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_id=message_id,
            disable_notification=disable_notification,
            protect_content=protect_content
        ))

    async def copy_message(
        self,
        chat_id: Union[str, int],
        from_chat_id: Union[str, int],
        message_id: int,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> MessageId:
        return await self(CopyMessage(
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_id=message_id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def send_photo(
        self,
        chat_id: Union[str, int],
        photo: Union[InputFile, str],
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        return await self(SendPhoto(
            chat_id=chat_id,
            photo=photo,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def send_audio(
        self,
        chat_id: Union[str, int],
        audio: Union[InputFile, str],
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        duration: Optional[int] = None,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        thumb: Optional[Union[InputFile, str]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        return await self(SendAudio(
            chat_id=chat_id,
            audio=audio,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            duration=duration,
            performer=performer,
            title=title,
            thumb=thumb,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def send_document(
        self,
        chat_id: Union[str, int],
        document: Union[InputFile, str],
        thumb: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        disable_content_type_detection: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        return await self(SendDocument(
            chat_id=chat_id,
            document=document,
            thumb=thumb,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            disable_content_type_detection=disable_content_type_detection,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def send_video(
        self,
        chat_id: Union[str, int],
        video: Union[InputFile, str],
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumb: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        supports_streaming: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        return await self(SendVideo(
            chat_id=chat_id,
            video=video,
            duration=duration,
            width=width,
            height=height,
            thumb=thumb,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            supports_streaming=supports_streaming,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def send_animation(
        self,
        chat_id: Union[str, int],
        animation: Union[InputFile, str],
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumb: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        return await self(SendAnimation(
            chat_id=chat_id,
            animation=animation,
            duration=duration,
            width=width,
            height=height,
            thumb=thumb,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def send_voice(
        self,
        chat_id: Union[str, int],
        voice: Union[InputFile, str],
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        duration: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        return await self(SendVoice(
            chat_id=chat_id,
            voice=voice,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            duration=duration,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def send_video_note(
        self,
        chat_id: Union[str, int],
        video_note: Union[InputFile, str],
        duration: Optional[int] = None,
        length: Optional[int] = None,
        thumb: Optional[Union[InputFile, str]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        return await self(SendVideoNote(
            chat_id=chat_id,
            video_note=video_note,
            duration=duration,
            length=length,
            thumb=thumb,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def send_media_group(
        self,
        chat_id: Union[str, int],
        media: List[Union[InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo]],
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None
    ) -> List[Message]:
        return await self(SendMediaGroup(
            chat_id=chat_id,
            media=media,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply
        ))

    async def send_location(
        self,
        chat_id: Union[str, int],
        latitude: float,
        longitude: float,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        return await self(SendLocation(
            chat_id=chat_id,
            latitude=latitude,
            longitude=longitude,
            horizontal_accuracy=horizontal_accuracy,
            live_period=live_period,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def edit_message_live_location(
        self,
        latitude: float,
        longitude: float,
        chat_id: Optional[Union[str, int]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        horizontal_accuracy: Optional[float] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, bool]:
        return await self(EditMessageLiveLocation(
            latitude=latitude,
            longitude=longitude,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            horizontal_accuracy=horizontal_accuracy,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
            reply_markup=reply_markup
        ))

    async def stop_message_live_location(
        self,
        chat_id: Optional[Union[str, int]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, bool]:
        return await self(StopMessageLiveLocation(
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            reply_markup=reply_markup
        ))

    async def send_venue(
        self,
        chat_id: Union[str, int],
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        return await self(SendVenue(
            chat_id=chat_id,
            latitude=latitude,
            longitude=longitude,
            title=title,
            address=address,
            foursquare_id=foursquare_id,
            foursquare_type=foursquare_type,
            google_place_id=google_place_id,
            google_place_type=google_place_type,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def send_contact(
        self,
        chat_id: Union[str, int],
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        return await self(SendContact(
            chat_id=chat_id,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            vcard=vcard,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def send_poll(
        self,
        chat_id: Union[str, int],
        question: str,
        options: List[str],
        is_anonymous: Optional[bool] = None,
        type_: Optional[str] = None,
        allows_multiple_answers: Optional[bool] = None,
        correct_option_id: Optional[int] = None,
        explanation: Optional[str] = None,
        explanation_parse_mode: Optional[str] = None,
        explanation_entities: Optional[List[MessageEntity]] = None,
        open_period: Optional[int] = None,
        close_date: Optional[int] = None,
        is_closed: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        return await self(SendPoll(
            chat_id=chat_id,
            question=question,
            options=options,
            is_anonymous=is_anonymous,
            type_=type_,
            allows_multiple_answers=allows_multiple_answers,
            correct_option_id=correct_option_id,
            explanation=explanation,
            explanation_parse_mode=explanation_parse_mode,
            explanation_entities=explanation_entities,
            open_period=open_period,
            close_date=close_date,
            is_closed=is_closed,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def send_dice(
        self,
        chat_id: Union[str, int],
        emoji: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        return await self(SendDice(
            chat_id=chat_id,
            emoji=emoji,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def send_chat_action(
        self,
        chat_id: Union[str, int],
        action: str
    ) -> bool:
        return await self(SendChatAction(
            chat_id=chat_id,
            action=action
        ))

    async def get_user_profile_photos(
        self,
        user_id: int,
        offset: Optional[int] = None,
        limit: Optional[int] = None
    ) -> UserProfilePhotos:
        return await self(GetUserProfilePhotos(
            user_id=user_id,
            offset=offset,
            limit=limit
        ))

    async def get_file(
        self,
        file_id: str
    ) -> File:
        return await self(GetFile(
            file_id=file_id
        ))

    async def ban_chat_member(
        self,
        chat_id: Union[str, int],
        user_id: int,
        until_date: Optional[int] = None,
        revoke_messages: Optional[bool] = None
    ) -> bool:
        return await self(BanChatMember(
            chat_id=chat_id,
            user_id=user_id,
            until_date=until_date,
            revoke_messages=revoke_messages
        ))

    async def unban_chat_member(
        self,
        chat_id: Union[str, int],
        user_id: int,
        only_if_banned: Optional[bool] = None
    ) -> bool:
        return await self(UnbanChatMember(
            chat_id=chat_id,
            user_id=user_id,
            only_if_banned=only_if_banned
        ))

    async def restrict_chat_member(
        self,
        chat_id: Union[str, int],
        user_id: int,
        permissions: ChatPermissions,
        until_date: Optional[int] = None
    ) -> bool:
        return await self(RestrictChatMember(
            chat_id=chat_id,
            user_id=user_id,
            permissions=permissions,
            until_date=until_date
        ))

    async def promote_chat_member(
        self,
        chat_id: Union[str, int],
        user_id: int,
        is_anonymous: Optional[bool] = None,
        can_manage_chat: Optional[bool] = None,
        can_post_messages: Optional[bool] = None,
        can_edit_messages: Optional[bool] = None,
        can_delete_messages: Optional[bool] = None,
        can_manage_voice_chats: Optional[bool] = None,
        can_restrict_members: Optional[bool] = None,
        can_promote_members: Optional[bool] = None,
        can_change_info: Optional[bool] = None,
        can_invite_users: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None
    ) -> bool:
        return await self(PromoteChatMember(
            chat_id=chat_id,
            user_id=user_id,
            is_anonymous=is_anonymous,
            can_manage_chat=can_manage_chat,
            can_post_messages=can_post_messages,
            can_edit_messages=can_edit_messages,
            can_delete_messages=can_delete_messages,
            can_manage_voice_chats=can_manage_voice_chats,
            can_restrict_members=can_restrict_members,
            can_promote_members=can_promote_members,
            can_change_info=can_change_info,
            can_invite_users=can_invite_users,
            can_pin_messages=can_pin_messages
        ))

    async def set_chat_administrator_custom_title(
        self,
        chat_id: Union[str, int],
        user_id: int,
        custom_title: str
    ) -> bool:
        return await self(SetChatAdministratorCustomTitle(
            chat_id=chat_id,
            user_id=user_id,
            custom_title=custom_title
        ))

    async def ban_chat_sender_chat(
        self,
        chat_id: Union[str, int],
        sender_chat_id: int
    ) -> bool:
        return await self(BanChatSenderChat(
            chat_id=chat_id,
            sender_chat_id=sender_chat_id
        ))

    async def unban_chat_sender_chat(
        self,
        chat_id: Union[str, int],
        sender_chat_id: int
    ) -> bool:
        return await self(UnbanChatSenderChat(
            chat_id=chat_id,
            sender_chat_id=sender_chat_id
        ))

    async def set_chat_permissions(
        self,
        chat_id: Union[str, int],
        permissions: ChatPermissions
    ) -> bool:
        return await self(SetChatPermissions(
            chat_id=chat_id,
            permissions=permissions
        ))

    async def export_chat_invite_link(
        self,
        chat_id: Union[str, int]
    ) -> str:
        return await self(ExportChatInviteLink(
            chat_id=chat_id
        ))

    async def create_chat_invite_link(
        self,
        chat_id: Union[str, int],
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        creates_join_request: Optional[bool] = None
    ) -> ChatInviteLink:
        return await self(CreateChatInviteLink(
            chat_id=chat_id,
            name=name,
            expire_date=expire_date,
            member_limit=member_limit,
            creates_join_request=creates_join_request
        ))

    async def edit_chat_invite_link(
        self,
        chat_id: Union[str, int],
        invite_link: str,
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        creates_join_request: Optional[bool] = None
    ) -> ChatInviteLink:
        return await self(EditChatInviteLink(
            chat_id=chat_id,
            invite_link=invite_link,
            name=name,
            expire_date=expire_date,
            member_limit=member_limit,
            creates_join_request=creates_join_request
        ))

    async def revoke_chat_invite_link(
        self,
        chat_id: Union[str, int],
        invite_link: str
    ) -> ChatInviteLink:
        return await self(RevokeChatInviteLink(
            chat_id=chat_id,
            invite_link=invite_link
        ))

    async def approve_chat_join_request(
        self,
        chat_id: Union[str, int],
        user_id: int
    ) -> bool:
        return await self(ApproveChatJoinRequest(
            chat_id=chat_id,
            user_id=user_id
        ))

    async def decline_chat_join_request(
        self,
        chat_id: Union[str, int],
        user_id: int
    ) -> bool:
        return await self(DeclineChatJoinRequest(
            chat_id=chat_id,
            user_id=user_id
        ))

    async def set_chat_photo(
        self,
        chat_id: Union[str, int],
        photo: InputFile
    ) -> bool:
        return await self(SetChatPhoto(
            chat_id=chat_id,
            photo=photo
        ))

    async def delete_chat_photo(
        self,
        chat_id: Union[str, int]
    ) -> bool:
        return await self(DeleteChatPhoto(
            chat_id=chat_id
        ))

    async def set_chat_title(
        self,
        chat_id: Union[str, int],
        title: str
    ) -> bool:
        return await self(SetChatTitle(
            chat_id=chat_id,
            title=title
        ))

    async def set_chat_description(
        self,
        chat_id: Union[str, int],
        description: Optional[str] = None
    ) -> bool:
        return await self(SetChatDescription(
            chat_id=chat_id,
            description=description
        ))

    async def pin_chat_message(
        self,
        chat_id: Union[str, int],
        message_id: int,
        disable_notification: Optional[bool] = None
    ) -> bool:
        return await self(PinChatMessage(
            chat_id=chat_id,
            message_id=message_id,
            disable_notification=disable_notification
        ))

    async def unpin_chat_message(
        self,
        chat_id: Union[str, int],
        message_id: Optional[int] = None
    ) -> bool:
        return await self(UnpinChatMessage(
            chat_id=chat_id,
            message_id=message_id
        ))

    async def unpin_all_chat_messages(
        self,
        chat_id: Union[str, int]
    ) -> bool:
        return await self(UnpinAllChatMessages(
            chat_id=chat_id
        ))

    async def leave_chat(
        self,
        chat_id: Union[str, int]
    ) -> bool:
        return await self(LeaveChat(
            chat_id=chat_id
        ))

    async def get_chat(
        self,
        chat_id: Union[str, int]
    ) -> ChatInfo:
        return await self(GetChat(
            chat_id=chat_id
        ))

    async def get_chat_administrators(
        self,
        chat_id: Union[str, int]
    ) -> List[ChatMember]:
        return await self(GetChatAdministrators(
            chat_id=chat_id
        ))

    async def get_chat_member_count(
        self,
        chat_id: Union[str, int]
    ) -> int:
        return await self(GetChatMemberCount(
            chat_id=chat_id
        ))

    async def get_chat_member(
        self,
        chat_id: Union[str, int],
        user_id: int
    ) -> ChatMember:
        return await self(GetChatMember(
            chat_id=chat_id,
            user_id=user_id
        ))

    async def set_chat_sticker_set(
        self,
        chat_id: Union[str, int],
        sticker_set_name: str
    ) -> bool:
        return await self(SetChatStickerSet(
            chat_id=chat_id,
            sticker_set_name=sticker_set_name
        ))

    async def delete_chat_sticker_set(
        self,
        chat_id: Union[str, int]
    ) -> bool:
        return await self(DeleteChatStickerSet(
            chat_id=chat_id
        ))

    async def answer_callback_query(
        self,
        callback_query_id: str,
        text: Optional[str] = None,
        show_alert: Optional[bool] = None,
        url: Optional[str] = None,
        cache_time: Optional[int] = None
    ) -> bool:
        return await self(AnswerCallbackQuery(
            callback_query_id=callback_query_id,
            text=text,
            show_alert=show_alert,
            url=url,
            cache_time=cache_time
        ))

    async def set_my_commands(
        self,
        commands: List[BotCommand],
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None
    ) -> bool:
        return await self(SetMyCommands(
            commands=commands,
            scope=scope,
            language_code=language_code
        ))

    async def delete_my_commands(
        self,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None
    ) -> bool:
        return await self(DeleteMyCommands(
            scope=scope,
            language_code=language_code
        ))

    async def get_my_commands(
        self,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None
    ) -> List[BotCommand]:
        return await self(GetMyCommands(
            scope=scope,
            language_code=language_code
        ))

    async def edit_message_text(
        self,
        text: str,
        chat_id: Optional[Union[str, int]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        parse_mode: Optional[str] = None,
        entities: Optional[List[MessageEntity]] = None,
        disable_web_page_preview: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, bool]:
        return await self(EditMessageText(
            text=text,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            parse_mode=parse_mode,
            entities=entities,
            disable_web_page_preview=disable_web_page_preview,
            reply_markup=reply_markup
        ))

    async def edit_message_caption(
        self,
        chat_id: Optional[Union[str, int]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, bool]:
        return await self(EditMessageCaption(
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            reply_markup=reply_markup
        ))

    async def edit_message_media(
        self,
        media: InputMedia,
        chat_id: Optional[Union[str, int]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, bool]:
        return await self(EditMessageMedia(
            media=media,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            reply_markup=reply_markup
        ))

    async def edit_message_reply_markup(
        self,
        chat_id: Optional[Union[str, int]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, bool]:
        return await self(EditMessageReplyMarkup(
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            reply_markup=reply_markup
        ))

    async def stop_poll(
        self,
        chat_id: Union[str, int],
        message_id: int,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Poll:
        return await self(StopPoll(
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=reply_markup
        ))

    async def delete_message(
        self,
        chat_id: Union[str, int],
        message_id: int
    ) -> bool:
        return await self(DeleteMessage(
            chat_id=chat_id,
            message_id=message_id
        ))

    async def send_sticker(
        self,
        chat_id: Union[str, int],
        sticker: Union[InputFile, str],
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        return await self(SendSticker(
            chat_id=chat_id,
            sticker=sticker,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def get_sticker_set(
        self,
        name: str
    ) -> StickerSet:
        return await self(GetStickerSet(
            name=name
        ))

    async def upload_sticker_file(
        self,
        user_id: int,
        png_sticker: InputFile
    ) -> File:
        return await self(UploadStickerFile(
            user_id=user_id,
            png_sticker=png_sticker
        ))

    async def create_new_sticker_set(
        self,
        user_id: int,
        name: str,
        title: str,
        emojis: str,
        png_sticker: Optional[Union[InputFile, str]] = None,
        tgs_sticker: Optional[InputFile] = None,
        contains_masks: Optional[bool] = None,
        mask_position: Optional[MaskPosition] = None
    ) -> bool:
        return await self(CreateNewStickerSet(
            user_id=user_id,
            name=name,
            title=title,
            emojis=emojis,
            png_sticker=png_sticker,
            tgs_sticker=tgs_sticker,
            contains_masks=contains_masks,
            mask_position=mask_position
        ))

    async def add_sticker_to_set(
        self,
        user_id: int,
        name: str,
        emojis: str,
        png_sticker: Optional[Union[InputFile, str]] = None,
        tgs_sticker: Optional[InputFile] = None,
        mask_position: Optional[MaskPosition] = None
    ) -> bool:
        return await self(AddStickerToSet(
            user_id=user_id,
            name=name,
            emojis=emojis,
            png_sticker=png_sticker,
            tgs_sticker=tgs_sticker,
            mask_position=mask_position
        ))

    async def set_sticker_position_in_set(
        self,
        sticker: str,
        position: int
    ) -> bool:
        return await self(SetStickerPositionInSet(
            sticker=sticker,
            position=position
        ))

    async def delete_sticker_from_set(
        self,
        sticker: str
    ) -> bool:
        return await self(DeleteStickerFromSet(
            sticker=sticker
        ))

    async def set_sticker_set_thumb(
        self,
        name: str,
        user_id: int,
        thumb: Optional[Union[InputFile, str]] = None
    ) -> bool:
        return await self(SetStickerSetThumb(
            name=name,
            user_id=user_id,
            thumb=thumb
        ))

    async def answer_inline_query(
        self,
        inline_query_id: str,
        results: List[InlineQueryResult],
        cache_time: Optional[int] = None,
        is_personal: Optional[bool] = None,
        next_offset: Optional[str] = None,
        switch_pm_text: Optional[str] = None,
        switch_pm_parameter: Optional[str] = None
    ) -> bool:
        return await self(AnswerInlineQuery(
            inline_query_id=inline_query_id,
            results=results,
            cache_time=cache_time,
            is_personal=is_personal,
            next_offset=next_offset,
            switch_pm_text=switch_pm_text,
            switch_pm_parameter=switch_pm_parameter
        ))

    async def send_invoice(
        self,
        chat_id: Union[str, int],
        title: str,
        description: str,
        payload: str,
        provider_token: str,
        currency: str,
        prices: List[LabeledPrice],
        max_tip_amount: Optional[int] = None,
        suggested_tip_amounts: Optional[List[int]] = None,
        start_parameter: Optional[str] = None,
        provider_data: Optional[str] = None,
        photo_url: Optional[str] = None,
        photo_size: Optional[int] = None,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        need_name: Optional[bool] = None,
        need_phone_number: Optional[bool] = None,
        need_email: Optional[bool] = None,
        need_shipping_address: Optional[bool] = None,
        send_phone_number_to_provider: Optional[bool] = None,
        send_email_to_provider: Optional[bool] = None,
        is_flexible: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Message:
        return await self(SendInvoice(
            chat_id=chat_id,
            title=title,
            description=description,
            payload=payload,
            provider_token=provider_token,
            currency=currency,
            prices=prices,
            max_tip_amount=max_tip_amount,
            suggested_tip_amounts=suggested_tip_amounts,
            start_parameter=start_parameter,
            provider_data=provider_data,
            photo_url=photo_url,
            photo_size=photo_size,
            photo_width=photo_width,
            photo_height=photo_height,
            need_name=need_name,
            need_phone_number=need_phone_number,
            need_email=need_email,
            need_shipping_address=need_shipping_address,
            send_phone_number_to_provider=send_phone_number_to_provider,
            send_email_to_provider=send_email_to_provider,
            is_flexible=is_flexible,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def answer_shipping_query(
        self,
        shipping_query_id: str,
        ok: bool,
        shipping_options: Optional[List[ShippingOption]] = None,
        error_message: Optional[str] = None
    ) -> bool:
        return await self(AnswerShippingQuery(
            shipping_query_id=shipping_query_id,
            ok=ok,
            shipping_options=shipping_options,
            error_message=error_message
        ))

    async def answer_pre_checkout_query(
        self,
        pre_checkout_query_id: str,
        ok: bool,
        error_message: Optional[str] = None
    ) -> bool:
        return await self(AnswerPreCheckoutQuery(
            pre_checkout_query_id=pre_checkout_query_id,
            ok=ok,
            error_message=error_message
        ))

    async def set_passport_data_errors(
        self,
        user_id: int,
        errors: List[PassportElementError]
    ) -> bool:
        return await self(SetPassportDataErrors(
            user_id=user_id,
            errors=errors
        ))

    async def send_game(
        self,
        chat_id: int,
        game_short_name: str,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Message:
        return await self(SendGame(
            chat_id=chat_id,
            game_short_name=game_short_name,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup
        ))

    async def set_game_score(
        self,
        user_id: int,
        score: int,
        force: Optional[bool] = None,
        disable_edit_message: Optional[bool] = None,
        chat_id: Optional[int] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None
    ) -> Union[Message, bool]:
        return await self(SetGameScore(
            user_id=user_id,
            score=score,
            force=force,
            disable_edit_message=disable_edit_message,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id
        ))

    async def get_game_high_scores(
        self,
        user_id: int,
        chat_id: Optional[int] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None
    ) -> List[GameHighScore]:
        return await self(GetGameHighScores(
            user_id=user_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id
        ))

