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
    WebhookInfo,
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
    UploadStickerFile,
)
from .base import SyncBaseBot


class Bot(SyncBaseBot):
    """
    Bot client for work with Telegram Bot API
    """

    def get_updates(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        allowed_updates: Optional[List[str]] = None,
    ) -> List[Update]:
        """
        Use this method to receive incoming updates using long
        polling (wiki). An Array of Update objects is returned.

        Reference: https://core.telegram.org/bots/api#getupdates

        :param offset: Identifier of the first update to be returned. Must be
        greater by one than the highest among the identifiers of
        previously received updates. By default, updates starting
        with the earliest unconfirmed update are returned. An update
        is considered confirmed as soon as getUpdates is called with
        an offset higher than its update_id. The negative offset can
        be specified to retrieve updates starting from -offset
        update from the end of the updates queue. All previous
        updates will forgotten.
        :param limit: Limits the number of updates to be retrieved. Values between
        1-100 are accepted. Defaults to 100.
        :param timeout: Timeout in seconds for long polling. Defaults to 0, i.e.
        usual short polling. Should be positive, short polling
        should be used for testing purposes only.
        :param allowed_updates: A JSON-serialized list of the update types you want your bot
        to receive. For example, specify [“message”,
        “edited_channel_post”, “callback_query”] to only receive
        updates of these types. See Update for a complete list of
        available update types. Specify an empty list to receive all
        update types except chat_member (default). If not specified,
        the previous setting will be used.Please note that this
        parameter doesn't affect updates created before the call to
        the getUpdates, so unwanted updates may be received for a
        short period of time.
        :returns: List[Update]
        """
        return self(
            GetUpdates(
                offset=offset,
                limit=limit,
                timeout=timeout,
                allowed_updates=allowed_updates,
            )
        )

    def set_webhook(
        self,
        url: str,
        certificate: Optional[InputFile] = None,
        ip_address: Optional[str] = None,
        max_connections: Optional[int] = None,
        allowed_updates: Optional[List[str]] = None,
        drop_pending_updates: Optional[bool] = None,
    ) -> bool:
        """
        Use this method to specify a url and receive incoming
        updates via an outgoing webhook. Whenever there is an update
        for the bot, we will send an HTTPS POST request to the
        specified url, containing a JSON-serialized Update. In case
        of an unsuccessful request, we will give up after a
        reasonable amount of attempts. Returns True on success.

        Reference: https://core.telegram.org/bots/api#setwebhook

        :param url: HTTPS url to send updates to. Use an empty string to remove
        webhook integration
        :param certificate: Upload your public key certificate so that the root
        certificate in use can be checked. See our self-signed guide
        for details.
        :param ip_address: The fixed IP address which will be used to send webhook
        requests instead of the IP address resolved through DNS
        :param max_connections: Maximum allowed number of simultaneous HTTPS connections to
        the webhook for update delivery, 1-100. Defaults to 40. Use
        lower values to limit the load on your bot's server, and
        higher values to increase your bot's throughput.
        :param allowed_updates: A JSON-serialized list of the update types you want your bot
        to receive. For example, specify [“message”,
        “edited_channel_post”, “callback_query”] to only receive
        updates of these types. See Update for a complete list of
        available update types. Specify an empty list to receive all
        update types except chat_member (default). If not specified,
        the previous setting will be used.Please note that this
        parameter doesn't affect updates created before the call to
        the setWebhook, so unwanted updates may be received for a
        short period of time.
        :param drop_pending_updates: Pass True to drop all pending updates
        :returns: bool
        """
        return self(
            SetWebhook(
                url=url,
                certificate=certificate,
                ip_address=ip_address,
                max_connections=max_connections,
                allowed_updates=allowed_updates,
                drop_pending_updates=drop_pending_updates,
            )
        )

    def delete_webhook(self, drop_pending_updates: Optional[bool] = None) -> bool:
        """
        Use this method to remove webhook integration if you decide
        to switch back to getUpdates. Returns True on success.

        Reference: https://core.telegram.org/bots/api#deletewebhook

        :param drop_pending_updates: Pass True to drop all pending updates
        :returns: bool
        """
        return self(DeleteWebhook(drop_pending_updates=drop_pending_updates))

    def get_webhook_info(
        self,
    ) -> WebhookInfo:
        """
        Use this method to get current webhook status. Requires no
        parameters. On success, returns a WebhookInfo object. If the
        bot is using getUpdates, will return an object with the url
        field empty.

        Reference: https://core.telegram.org/bots/api#getwebhookinfo

        :returns: WebhookInfo
        """
        return self(GetWebhookInfo())

    def get_me(
        self,
    ) -> User:
        """
        A simple method for testing your bot's authentication token.
        Requires no parameters. Returns basic information about the
        bot in form of a User object.

        Reference: https://core.telegram.org/bots/api#getme

        :returns: User
        """
        return self(GetMe())

    def log_out(
        self,
    ) -> bool:
        """
        Use this method to log out from the cloud Bot API server
        before launching the bot locally. You must log out the bot
        before running it locally, otherwise there is no guarantee
        that the bot will receive updates. After a successful call,
        you can immediately log in on a local server, but will not
        be able to log in back to the cloud Bot API server for 10
        minutes. Returns True on success. Requires no parameters.

        Reference: https://core.telegram.org/bots/api#logout

        :returns: bool
        """
        return self(LogOut())

    def close(
        self,
    ) -> bool:
        """
        Use this method to close the bot instance before moving it
        from one local server to another. You need to delete the
        webhook before calling this method to ensure that the bot
        isn't launched again after server restart. The method will
        return error 429 in the first 10 minutes after the bot is
        launched. Returns True on success. Requires no parameters.

        Reference: https://core.telegram.org/bots/api#close

        :returns: bool
        """
        return self(Close())

    def send_message(
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
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> Message:
        """
        Use this method to send text messages. On success, the sent
        Message is returned.

        Reference: https://core.telegram.org/bots/api#sendmessage

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param text: Text of the message to be sent, 1-4096 characters after
        entities parsing
        :param parse_mode: Mode for parsing entities in the message text. See
        formatting options for more details.
        :param entities: A JSON-serialized list of special entities that appear in
        message text, which can be specified instead of parse_mode
        :param disable_web_page_preview: Disables link previews for links in this message
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for
        an inline keyboard, custom reply keyboard, instructions to
        remove reply keyboard or to force a reply from the user.
        :returns: Message
        """
        return self(
            SendMessage(
                chat_id=chat_id,
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
        )

    def forward_message(
        self,
        chat_id: Union[str, int],
        from_chat_id: Union[str, int],
        message_id: int,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
    ) -> Message:
        """
        Use this method to forward messages of any kind. Service
        messages can't be forwarded. On success, the sent Message is
        returned.

        Reference: https://core.telegram.org/bots/api#forwardmessage

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param from_chat_id: Unique identifier for the chat where the original message
        was sent (or channel username in the format
        @channelusername)
        :param message_id: Message identifier in the chat specified in from_chat_id
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the forwarded message from
        forwarding and saving
        :returns: Message
        """
        return self(
            ForwardMessage(
                chat_id=chat_id,
                from_chat_id=from_chat_id,
                message_id=message_id,
                disable_notification=disable_notification,
                protect_content=protect_content,
            )
        )

    def copy_message(
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
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> MessageId:
        """
        Use this method to copy messages of any kind. Service
        messages and invoice messages can't be copied. The method is
        analogous to the method forwardMessage, but the copied
        message doesn't have a link to the original message. Returns
        the MessageId of the sent message on success.

        Reference: https://core.telegram.org/bots/api#copymessage

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param from_chat_id: Unique identifier for the chat where the original message
        was sent (or channel username in the format
        @channelusername)
        :param message_id: Message identifier in the chat specified in from_chat_id
        :param caption: New caption for media, 0-1024 characters after entities
        parsing. If not specified, the original caption is kept
        :param parse_mode: Mode for parsing entities in the new caption. See formatting
        options for more details.
        :param caption_entities: A JSON-serialized list of special entities that appear in
        the new caption, which can be specified instead of
        parse_mode
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for
        an inline keyboard, custom reply keyboard, instructions to
        remove reply keyboard or to force a reply from the user.
        :returns: MessageId
        """
        return self(
            CopyMessage(
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
                reply_markup=reply_markup,
            )
        )

    def send_photo(
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
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> Message:
        """
        Use this method to send photos. On success, the sent Message
        is returned.

        Reference: https://core.telegram.org/bots/api#sendphoto

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param photo: Photo to send. Pass a file_id as String to send a photo that
        exists on the Telegram servers (recommended), pass an HTTP
        URL as a String for Telegram to get a photo from the
        Internet, or upload a new photo using multipart/form-data.
        The photo must be at most 10 MB in size. The photo's width
        and height must not exceed 10000 in total. Width and height
        ratio must be at most 20. More info on Sending Files »
        :param caption: Photo caption (may also be used when resending photos by
        file_id), 0-1024 characters after entities parsing
        :param parse_mode: Mode for parsing entities in the photo caption. See
        formatting options for more details.
        :param caption_entities: A JSON-serialized list of special entities that appear in
        the caption, which can be specified instead of parse_mode
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for
        an inline keyboard, custom reply keyboard, instructions to
        remove reply keyboard or to force a reply from the user.
        :returns: Message
        """
        return self(
            SendPhoto(
                chat_id=chat_id,
                photo=photo,
                caption=caption,
                parse_mode=parse_mode,
                caption_entities=caption_entities,
                disable_notification=disable_notification,
                protect_content=protect_content,
                reply_to_message_id=reply_to_message_id,
                allow_sending_without_reply=allow_sending_without_reply,
                reply_markup=reply_markup,
            )
        )

    def send_audio(
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
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> Message:
        """
        Use this method to send audio files, if you want Telegram
        clients to display them in the music player. Your audio must
        be in the .MP3 or .M4A format. On success, the sent Message
        is returned. Bots can currently send audio files of up to 50
        MB in size, this limit may be changed in the future.

        Reference: https://core.telegram.org/bots/api#sendaudio

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param audio: Audio file to send. Pass a file_id as String to send an
        audio file that exists on the Telegram servers
        (recommended), pass an HTTP URL as a String for Telegram to
        get an audio file from the Internet, or upload a new one
        using multipart/form-data. More info on Sending Files »
        :param caption: Audio caption, 0-1024 characters after entities parsing
        :param parse_mode: Mode for parsing entities in the audio caption. See
        formatting options for more details.
        :param caption_entities: A JSON-serialized list of special entities that appear in
        the caption, which can be specified instead of parse_mode
        :param duration: Duration of the audio in seconds
        :param performer: Performer
        :param title: Track name
        :param thumb: Thumbnail of the file sent; can be ignored if thumbnail
        generation for the file is supported server-side. The
        thumbnail should be in JPEG format and less than 200 kB in
        size. A thumbnail's width and height should not exceed 320.
        Ignored if the file is not uploaded using multipart/form-
        data. Thumbnails can't be reused and can be only uploaded as
        a new file, so you can pass “attach://<file_attach_name>” if
        the thumbnail was uploaded using multipart/form-data under
        <file_attach_name>. More info on Sending Files »
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for
        an inline keyboard, custom reply keyboard, instructions to
        remove reply keyboard or to force a reply from the user.
        :returns: Message
        """
        return self(
            SendAudio(
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
                reply_markup=reply_markup,
            )
        )

    def send_document(
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
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> Message:
        """
        Use this method to send general files. On success, the sent
        Message is returned. Bots can currently send files of any
        type of up to 50 MB in size, this limit may be changed in
        the future.

        Reference: https://core.telegram.org/bots/api#senddocument

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param document: File to send. Pass a file_id as String to send a file that
        exists on the Telegram servers (recommended), pass an HTTP
        URL as a String for Telegram to get a file from the
        Internet, or upload a new one using multipart/form-data.
        More info on Sending Files »
        :param thumb: Thumbnail of the file sent; can be ignored if thumbnail
        generation for the file is supported server-side. The
        thumbnail should be in JPEG format and less than 200 kB in
        size. A thumbnail's width and height should not exceed 320.
        Ignored if the file is not uploaded using multipart/form-
        data. Thumbnails can't be reused and can be only uploaded as
        a new file, so you can pass “attach://<file_attach_name>” if
        the thumbnail was uploaded using multipart/form-data under
        <file_attach_name>. More info on Sending Files »
        :param caption: Document caption (may also be used when resending documents
        by file_id), 0-1024 characters after entities parsing
        :param parse_mode: Mode for parsing entities in the document caption. See
        formatting options for more details.
        :param caption_entities: A JSON-serialized list of special entities that appear in
        the caption, which can be specified instead of parse_mode
        :param disable_content_type_detection: Disables automatic server-side content type detection for
        files uploaded using multipart/form-data
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for
        an inline keyboard, custom reply keyboard, instructions to
        remove reply keyboard or to force a reply from the user.
        :returns: Message
        """
        return self(
            SendDocument(
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
                reply_markup=reply_markup,
            )
        )

    def send_video(
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
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> Message:
        """
        Use this method to send video files, Telegram clients
        support mp4 videos (other formats may be sent as Document).
        On success, the sent Message is returned. Bots can currently
        send video files of up to 50 MB in size, this limit may be
        changed in the future.

        Reference: https://core.telegram.org/bots/api#sendvideo

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param video: Video to send. Pass a file_id as String to send a video that
        exists on the Telegram servers (recommended), pass an HTTP
        URL as a String for Telegram to get a video from the
        Internet, or upload a new video using multipart/form-data.
        More info on Sending Files »
        :param duration: Duration of sent video in seconds
        :param width: Video width
        :param height: Video height
        :param thumb: Thumbnail of the file sent; can be ignored if thumbnail
        generation for the file is supported server-side. The
        thumbnail should be in JPEG format and less than 200 kB in
        size. A thumbnail's width and height should not exceed 320.
        Ignored if the file is not uploaded using multipart/form-
        data. Thumbnails can't be reused and can be only uploaded as
        a new file, so you can pass “attach://<file_attach_name>” if
        the thumbnail was uploaded using multipart/form-data under
        <file_attach_name>. More info on Sending Files »
        :param caption: Video caption (may also be used when resending videos by
        file_id), 0-1024 characters after entities parsing
        :param parse_mode: Mode for parsing entities in the video caption. See
        formatting options for more details.
        :param caption_entities: A JSON-serialized list of special entities that appear in
        the caption, which can be specified instead of parse_mode
        :param supports_streaming: Pass True, if the uploaded video is suitable for streaming
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for
        an inline keyboard, custom reply keyboard, instructions to
        remove reply keyboard or to force a reply from the user.
        :returns: Message
        """
        return self(
            SendVideo(
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
                reply_markup=reply_markup,
            )
        )

    def send_animation(
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
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> Message:
        """
        Use this method to send animation files (GIF or H.264/MPEG-4
        AVC video without sound). On success, the sent Message is
        returned. Bots can currently send animation files of up to
        50 MB in size, this limit may be changed in the future.

        Reference: https://core.telegram.org/bots/api#sendanimation

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param animation: Animation to send. Pass a file_id as String to send an
        animation that exists on the Telegram servers (recommended),
        pass an HTTP URL as a String for Telegram to get an
        animation from the Internet, or upload a new animation using
        multipart/form-data. More info on Sending Files »
        :param duration: Duration of sent animation in seconds
        :param width: Animation width
        :param height: Animation height
        :param thumb: Thumbnail of the file sent; can be ignored if thumbnail
        generation for the file is supported server-side. The
        thumbnail should be in JPEG format and less than 200 kB in
        size. A thumbnail's width and height should not exceed 320.
        Ignored if the file is not uploaded using multipart/form-
        data. Thumbnails can't be reused and can be only uploaded as
        a new file, so you can pass “attach://<file_attach_name>” if
        the thumbnail was uploaded using multipart/form-data under
        <file_attach_name>. More info on Sending Files »
        :param caption: Animation caption (may also be used when resending animation
        by file_id), 0-1024 characters after entities parsing
        :param parse_mode: Mode for parsing entities in the animation caption. See
        formatting options for more details.
        :param caption_entities: A JSON-serialized list of special entities that appear in
        the caption, which can be specified instead of parse_mode
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for
        an inline keyboard, custom reply keyboard, instructions to
        remove reply keyboard or to force a reply from the user.
        :returns: Message
        """
        return self(
            SendAnimation(
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
                reply_markup=reply_markup,
            )
        )

    def send_voice(
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
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> Message:
        """
        Use this method to send audio files, if you want Telegram
        clients to display the file as a playable voice message. For
        this to work, your audio must be in an .OGG file encoded
        with OPUS (other formats may be sent as Audio or Document).
        On success, the sent Message is returned. Bots can currently
        send voice messages of up to 50 MB in size, this limit may
        be changed in the future.

        Reference: https://core.telegram.org/bots/api#sendvoice

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param voice: Audio file to send. Pass a file_id as String to send a file
        that exists on the Telegram servers (recommended), pass an
        HTTP URL as a String for Telegram to get a file from the
        Internet, or upload a new one using multipart/form-data.
        More info on Sending Files »
        :param caption: Voice message caption, 0-1024 characters after entities
        parsing
        :param parse_mode: Mode for parsing entities in the voice message caption. See
        formatting options for more details.
        :param caption_entities: A JSON-serialized list of special entities that appear in
        the caption, which can be specified instead of parse_mode
        :param duration: Duration of the voice message in seconds
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for
        an inline keyboard, custom reply keyboard, instructions to
        remove reply keyboard or to force a reply from the user.
        :returns: Message
        """
        return self(
            SendVoice(
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
                reply_markup=reply_markup,
            )
        )

    def send_video_note(
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
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> Message:
        """
        As of v.4.0, Telegram clients support rounded square mp4
        videos of up to 1 minute long. Use this method to send video
        messages. On success, the sent Message is returned.

        Reference: https://core.telegram.org/bots/api#sendvideonote

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param video_note: Video note to send. Pass a file_id as String to send a video
        note that exists on the Telegram servers (recommended) or
        upload a new video using multipart/form-data. More info on
        Sending Files ». Sending video notes by a URL is currently
        unsupported
        :param duration: Duration of sent video in seconds
        :param length: Video width and height, i.e. diameter of the video message
        :param thumb: Thumbnail of the file sent; can be ignored if thumbnail
        generation for the file is supported server-side. The
        thumbnail should be in JPEG format and less than 200 kB in
        size. A thumbnail's width and height should not exceed 320.
        Ignored if the file is not uploaded using multipart/form-
        data. Thumbnails can't be reused and can be only uploaded as
        a new file, so you can pass “attach://<file_attach_name>” if
        the thumbnail was uploaded using multipart/form-data under
        <file_attach_name>. More info on Sending Files »
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for
        an inline keyboard, custom reply keyboard, instructions to
        remove reply keyboard or to force a reply from the user.
        :returns: Message
        """
        return self(
            SendVideoNote(
                chat_id=chat_id,
                video_note=video_note,
                duration=duration,
                length=length,
                thumb=thumb,
                disable_notification=disable_notification,
                protect_content=protect_content,
                reply_to_message_id=reply_to_message_id,
                allow_sending_without_reply=allow_sending_without_reply,
                reply_markup=reply_markup,
            )
        )

    def send_media_group(
        self,
        chat_id: Union[str, int],
        media: List[
            Union[InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo]
        ],
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
    ) -> List[Message]:
        """
        Use this method to send a group of photos, videos, documents
        or audios as an album. Documents and audio files can be only
        grouped in an album with messages of the same type. On
        success, an array of Messages that were sent is returned.

        Reference: https://core.telegram.org/bots/api#sendmediagroup

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param media: A JSON-serialized array describing messages to be sent, must
        include 2-10 items
        :param disable_notification: Sends messages silently. Users will receive a notification
        with no sound.
        :param protect_content: Protects the contents of the sent messages from forwarding
        and saving
        :param reply_to_message_id: If the messages are a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :returns: List[Message]
        """
        return self(
            SendMediaGroup(
                chat_id=chat_id,
                media=media,
                disable_notification=disable_notification,
                protect_content=protect_content,
                reply_to_message_id=reply_to_message_id,
                allow_sending_without_reply=allow_sending_without_reply,
            )
        )

    def send_location(
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
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> Message:
        """
        Use this method to send point on the map. On success, the
        sent Message is returned.

        Reference: https://core.telegram.org/bots/api#sendlocation

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param latitude: Latitude of the location
        :param longitude: Longitude of the location
        :param horizontal_accuracy: The radius of uncertainty for the location, measured in
        meters; 0-1500
        :param live_period: Period in seconds for which the location will be updated
        (see Live Locations, should be between 60 and 86400.
        :param heading: For live locations, a direction in which the user is moving,
        in degrees. Must be between 1 and 360 if specified.
        :param proximity_alert_radius: For live locations, a maximum distance for proximity alerts
        about approaching another chat member, in meters. Must be
        between 1 and 100000 if specified.
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for
        an inline keyboard, custom reply keyboard, instructions to
        remove reply keyboard or to force a reply from the user.
        :returns: Message
        """
        return self(
            SendLocation(
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
                reply_markup=reply_markup,
            )
        )

    def edit_message_live_location(
        self,
        latitude: float,
        longitude: float,
        chat_id: Optional[Union[str, int]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        horizontal_accuracy: Optional[float] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Union[Message, bool]:
        """
        Use this method to edit live location messages. A location
        can be edited until its live_period expires or editing is
        explicitly disabled by a call to stopMessageLiveLocation. On
        success, if the edited message is not an inline message, the
        edited Message is returned, otherwise True is returned.

        Reference: https://core.telegram.org/bots/api#editmessagelivelocation

        :param latitude: Latitude of new location
        :param longitude: Longitude of new location
        :param chat_id: Required if inline_message_id is not specified. Unique
        identifier for the target chat or username of the target
        channel (in the format @channelusername)
        :param message_id: Required if inline_message_id is not specified. Identifier
        of the message to edit
        :param inline_message_id: Required if chat_id and message_id are not specified.
        Identifier of the inline message
        :param horizontal_accuracy: The radius of uncertainty for the location, measured in
        meters; 0-1500
        :param heading: Direction in which the user is moving, in degrees. Must be
        between 1 and 360 if specified.
        :param proximity_alert_radius: Maximum distance for proximity alerts about approaching
        another chat member, in meters. Must be between 1 and 100000
        if specified.
        :param reply_markup: A JSON-serialized object for a new inline keyboard.
        :returns: Union[Message, bool]
        """
        return self(
            EditMessageLiveLocation(
                latitude=latitude,
                longitude=longitude,
                chat_id=chat_id,
                message_id=message_id,
                inline_message_id=inline_message_id,
                horizontal_accuracy=horizontal_accuracy,
                heading=heading,
                proximity_alert_radius=proximity_alert_radius,
                reply_markup=reply_markup,
            )
        )

    def stop_message_live_location(
        self,
        chat_id: Optional[Union[str, int]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Union[Message, bool]:
        """
        Use this method to stop updating a live location message
        before live_period expires. On success, if the message is
        not an inline message, the edited Message is returned,
        otherwise True is returned.

        Reference: https://core.telegram.org/bots/api#stopmessagelivelocation

        :param chat_id: Required if inline_message_id is not specified. Unique
        identifier for the target chat or username of the target
        channel (in the format @channelusername)
        :param message_id: Required if inline_message_id is not specified. Identifier
        of the message with live location to stop
        :param inline_message_id: Required if chat_id and message_id are not specified.
        Identifier of the inline message
        :param reply_markup: A JSON-serialized object for a new inline keyboard.
        :returns: Union[Message, bool]
        """
        return self(
            StopMessageLiveLocation(
                chat_id=chat_id,
                message_id=message_id,
                inline_message_id=inline_message_id,
                reply_markup=reply_markup,
            )
        )

    def send_venue(
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
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> Message:
        """
        Use this method to send information about a venue. On
        success, the sent Message is returned.

        Reference: https://core.telegram.org/bots/api#sendvenue

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param latitude: Latitude of the venue
        :param longitude: Longitude of the venue
        :param title: Name of the venue
        :param address: Address of the venue
        :param foursquare_id: Foursquare identifier of the venue
        :param foursquare_type: Foursquare type of the venue, if known. (For example,
        “arts_entertainment/default”, “arts_entertainment/aquarium”
        or “food/icecream”.)
        :param google_place_id: Google Places identifier of the venue
        :param google_place_type: Google Places type of the venue. (See supported types.)
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for
        an inline keyboard, custom reply keyboard, instructions to
        remove reply keyboard or to force a reply from the user.
        :returns: Message
        """
        return self(
            SendVenue(
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
                reply_markup=reply_markup,
            )
        )

    def send_contact(
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
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> Message:
        """
        Use this method to send phone contacts. On success, the sent
        Message is returned.

        Reference: https://core.telegram.org/bots/api#sendcontact

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param phone_number: Contact's phone number
        :param first_name: Contact's first name
        :param last_name: Contact's last name
        :param vcard: Additional data about the contact in the form of a vCard,
        0-2048 bytes
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for
        an inline keyboard, custom reply keyboard, instructions to
        remove keyboard or to force a reply from the user.
        :returns: Message
        """
        return self(
            SendContact(
                chat_id=chat_id,
                phone_number=phone_number,
                first_name=first_name,
                last_name=last_name,
                vcard=vcard,
                disable_notification=disable_notification,
                protect_content=protect_content,
                reply_to_message_id=reply_to_message_id,
                allow_sending_without_reply=allow_sending_without_reply,
                reply_markup=reply_markup,
            )
        )

    def send_poll(
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
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> Message:
        """
        Use this method to send a native poll. On success, the sent
        Message is returned.

        Reference: https://core.telegram.org/bots/api#sendpoll

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param question: Poll question, 1-300 characters
        :param options: A JSON-serialized list of answer options, 2-10 strings 1-100
        characters each
        :param is_anonymous: True, if the poll needs to be anonymous, defaults to True
        :param type_: Poll type, “quiz” or “regular”, defaults to “regular”
        :param allows_multiple_answers: True, if the poll allows multiple answers, ignored for polls
        in quiz mode, defaults to False
        :param correct_option_id: 0-based identifier of the correct answer option, required
        for polls in quiz mode
        :param explanation: Text that is shown when a user chooses an incorrect answer
        or taps on the lamp icon in a quiz-style poll, 0-200
        characters with at most 2 line feeds after entities parsing
        :param explanation_parse_mode: Mode for parsing entities in the explanation. See formatting
        options for more details.
        :param explanation_entities: A JSON-serialized list of special entities that appear in
        the poll explanation, which can be specified instead of
        parse_mode
        :param open_period: Amount of time in seconds the poll will be active after
        creation, 5-600. Can't be used together with close_date.
        :param close_date: Point in time (Unix timestamp) when the poll will be
        automatically closed. Must be at least 5 and no more than
        600 seconds in the future. Can't be used together with
        open_period.
        :param is_closed: Pass True, if the poll needs to be immediately closed. This
        can be useful for poll preview.
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for
        an inline keyboard, custom reply keyboard, instructions to
        remove reply keyboard or to force a reply from the user.
        :returns: Message
        """
        return self(
            SendPoll(
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
                reply_markup=reply_markup,
            )
        )

    def send_dice(
        self,
        chat_id: Union[str, int],
        emoji: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> Message:
        """
        Use this method to send an animated emoji that will display
        a random value. On success, the sent Message is returned.

        Reference: https://core.telegram.org/bots/api#senddice

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param emoji: Emoji on which the dice throw animation is based. Currently,
        must be one of “”, “”, “”, “”, “”, or “”. Dice can have
        values 1-6 for “”, “” and “”, values 1-5 for “” and “”, and
        values 1-64 for “”. Defaults to “”
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for
        an inline keyboard, custom reply keyboard, instructions to
        remove reply keyboard or to force a reply from the user.
        :returns: Message
        """
        return self(
            SendDice(
                chat_id=chat_id,
                emoji=emoji,
                disable_notification=disable_notification,
                protect_content=protect_content,
                reply_to_message_id=reply_to_message_id,
                allow_sending_without_reply=allow_sending_without_reply,
                reply_markup=reply_markup,
            )
        )

    def send_chat_action(self, chat_id: Union[str, int], action: str) -> bool:
        """
        Use this method when you need to tell the user that
        something is happening on the bot's side. The status is set
        for 5 seconds or less (when a message arrives from your bot,
        Telegram clients clear its typing status). Returns True on
        success.

        Reference: https://core.telegram.org/bots/api#sendchataction

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param action: Type of action to broadcast. Choose one, depending on what
        the user is about to receive: typing for text messages,
        upload_photo for photos, record_video or upload_video for
        videos, record_voice or upload_voice for voice notes,
        upload_document for general files, choose_sticker for
        stickers, find_location for location data, record_video_note
        or upload_video_note for video notes.
        :returns: bool
        """
        return self(SendChatAction(chat_id=chat_id, action=action))

    def get_user_profile_photos(
        self, user_id: int, offset: Optional[int] = None, limit: Optional[int] = None
    ) -> UserProfilePhotos:
        """
        Use this method to get a list of profile pictures for a
        user. Returns a UserProfilePhotos object.

        Reference: https://core.telegram.org/bots/api#getuserprofilephotos

        :param user_id: Unique identifier of the target user
        :param offset: Sequential number of the first photo to be returned. By
        default, all photos are returned.
        :param limit: Limits the number of photos to be retrieved. Values between
        1-100 are accepted. Defaults to 100.
        :returns: UserProfilePhotos
        """
        return self(GetUserProfilePhotos(user_id=user_id, offset=offset, limit=limit))

    def get_file(self, file_id: str) -> File:
        """
        Use this method to get basic info about a file and prepare
        it for downloading. For the moment, bots can download files
        of up to 20MB in size. On success, a File object is
        returned. The file can then be downloaded via the link
        https://api.telegram.org/file/bot<token>/<file_path>, where
        <file_path> is taken from the response. It is guaranteed
        that the link will be valid for at least 1 hour. When the
        link expires, a new one can be requested by calling getFile
        again.

        Reference: https://core.telegram.org/bots/api#getfile

        :param file_id: File identifier to get info about
        :returns: File
        """
        return self(GetFile(file_id=file_id))

    def ban_chat_member(
        self,
        chat_id: Union[str, int],
        user_id: int,
        until_date: Optional[int] = None,
        revoke_messages: Optional[bool] = None,
    ) -> bool:
        """
        Use this method to ban a user in a group, a supergroup or a
        channel. In the case of supergroups and channels, the user
        will not be able to return to the chat on their own using
        invite links, etc., unless unbanned first. The bot must be
        an administrator in the chat for this to work and must have
        the appropriate administrator rights. Returns True on
        success.

        Reference: https://core.telegram.org/bots/api#banchatmember

        :param chat_id: Unique identifier for the target group or username of the
        target supergroup or channel (in the format
        @channelusername)
        :param user_id: Unique identifier of the target user
        :param until_date: Date when the user will be unbanned, unix time. If user is
        banned for more than 366 days or less than 30 seconds from
        the current time they are considered to be banned forever.
        Applied for supergroups and channels only.
        :param revoke_messages: Pass True to delete all messages from the chat for the user
        that is being removed. If False, the user will be able to
        see messages in the group that were sent before the user was
        removed. Always True for supergroups and channels.
        :returns: bool
        """
        return self(
            BanChatMember(
                chat_id=chat_id,
                user_id=user_id,
                until_date=until_date,
                revoke_messages=revoke_messages,
            )
        )

    def unban_chat_member(
        self,
        chat_id: Union[str, int],
        user_id: int,
        only_if_banned: Optional[bool] = None,
    ) -> bool:
        """
        Use this method to unban a previously banned user in a
        supergroup or channel. The user will not return to the group
        or channel automatically, but will be able to join via link,
        etc. The bot must be an administrator for this to work. By
        default, this method guarantees that after the call the user
        is not a member of the chat, but will be able to join it. So
        if the user is a member of the chat they will also be
        removed from the chat. If you don't want this, use the
        parameter only_if_banned. Returns True on success.

        Reference: https://core.telegram.org/bots/api#unbanchatmember

        :param chat_id: Unique identifier for the target group or username of the
        target supergroup or channel (in the format
        @channelusername)
        :param user_id: Unique identifier of the target user
        :param only_if_banned: Do nothing if the user is not banned
        :returns: bool
        """
        return self(
            UnbanChatMember(
                chat_id=chat_id, user_id=user_id, only_if_banned=only_if_banned
            )
        )

    def restrict_chat_member(
        self,
        chat_id: Union[str, int],
        user_id: int,
        permissions: ChatPermissions,
        until_date: Optional[int] = None,
    ) -> bool:
        """
        Use this method to restrict a user in a supergroup. The bot
        must be an administrator in the supergroup for this to work
        and must have the appropriate administrator rights. Pass
        True for all permissions to lift restrictions from a user.
        Returns True on success.

        Reference: https://core.telegram.org/bots/api#restrictchatmember

        :param chat_id: Unique identifier for the target chat or username of the
        target supergroup (in the format @supergroupusername)
        :param user_id: Unique identifier of the target user
        :param permissions: A JSON-serialized object for new user permissions
        :param until_date: Date when restrictions will be lifted for the user, unix
        time. If user is restricted for more than 366 days or less
        than 30 seconds from the current time, they are considered
        to be restricted forever
        :returns: bool
        """
        return self(
            RestrictChatMember(
                chat_id=chat_id,
                user_id=user_id,
                permissions=permissions,
                until_date=until_date,
            )
        )

    def promote_chat_member(
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
        can_pin_messages: Optional[bool] = None,
    ) -> bool:
        """
        Use this method to promote or demote a user in a supergroup
        or a channel. The bot must be an administrator in the chat
        for this to work and must have the appropriate administrator
        rights. Pass False for all boolean parameters to demote a
        user. Returns True on success.

        Reference: https://core.telegram.org/bots/api#promotechatmember

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param user_id: Unique identifier of the target user
        :param is_anonymous: Pass True, if the administrator's presence in the chat is
        hidden
        :param can_manage_chat: Pass True, if the administrator can access the chat event
        log, chat statistics, message statistics in channels, see
        channel members, see anonymous administrators in supergroups
        and ignore slow mode. Implied by any other administrator
        privilege
        :param can_post_messages: Pass True, if the administrator can create channel posts,
        channels only
        :param can_edit_messages: Pass True, if the administrator can edit messages of other
        users and can pin messages, channels only
        :param can_delete_messages: Pass True, if the administrator can delete messages of other
        users
        :param can_manage_voice_chats: Pass True, if the administrator can manage voice chats
        :param can_restrict_members: Pass True, if the administrator can restrict, ban or unban
        chat members
        :param can_promote_members: Pass True, if the administrator can add new administrators
        with a subset of their own privileges or demote
        administrators that he has promoted, directly or indirectly
        (promoted by administrators that were appointed by him)
        :param can_change_info: Pass True, if the administrator can change chat title, photo
        and other settings
        :param can_invite_users: Pass True, if the administrator can invite new users to the
        chat
        :param can_pin_messages: Pass True, if the administrator can pin messages,
        supergroups only
        :returns: bool
        """
        return self(
            PromoteChatMember(
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
                can_pin_messages=can_pin_messages,
            )
        )

    def set_chat_administrator_custom_title(
        self, chat_id: Union[str, int], user_id: int, custom_title: str
    ) -> bool:
        """
        Use this method to set a custom title for an administrator
        in a supergroup promoted by the bot. Returns True on
        success.

        Reference: https://core.telegram.org/bots/api#setchatadministratorcustomtitle

        :param chat_id: Unique identifier for the target chat or username of the
        target supergroup (in the format @supergroupusername)
        :param user_id: Unique identifier of the target user
        :param custom_title: New custom title for the administrator; 0-16 characters,
        emoji are not allowed
        :returns: bool
        """
        return self(
            SetChatAdministratorCustomTitle(
                chat_id=chat_id, user_id=user_id, custom_title=custom_title
            )
        )

    def ban_chat_sender_chat(
        self, chat_id: Union[str, int], sender_chat_id: int
    ) -> bool:
        """
        Use this method to ban a channel chat in a supergroup or a
        channel. Until the chat is unbanned, the owner of the banned
        chat won't be able to send messages on behalf of any of
        their channels. The bot must be an administrator in the
        supergroup or channel for this to work and must have the
        appropriate administrator rights. Returns True on success.

        Reference: https://core.telegram.org/bots/api#banchatsenderchat

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param sender_chat_id: Unique identifier of the target sender chat
        :returns: bool
        """
        return self(BanChatSenderChat(chat_id=chat_id, sender_chat_id=sender_chat_id))

    def unban_chat_sender_chat(
        self, chat_id: Union[str, int], sender_chat_id: int
    ) -> bool:
        """
        Use this method to unban a previously banned channel chat in
        a supergroup or channel. The bot must be an administrator
        for this to work and must have the appropriate administrator
        rights. Returns True on success.

        Reference: https://core.telegram.org/bots/api#unbanchatsenderchat

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param sender_chat_id: Unique identifier of the target sender chat
        :returns: bool
        """
        return self(UnbanChatSenderChat(chat_id=chat_id, sender_chat_id=sender_chat_id))

    def set_chat_permissions(
        self, chat_id: Union[str, int], permissions: ChatPermissions
    ) -> bool:
        """
        Use this method to set default chat permissions for all
        members. The bot must be an administrator in the group or a
        supergroup for this to work and must have the
        can_restrict_members administrator rights. Returns True on
        success.

        Reference: https://core.telegram.org/bots/api#setchatpermissions

        :param chat_id: Unique identifier for the target chat or username of the
        target supergroup (in the format @supergroupusername)
        :param permissions: A JSON-serialized object for new default chat permissions
        :returns: bool
        """
        return self(SetChatPermissions(chat_id=chat_id, permissions=permissions))

    def export_chat_invite_link(self, chat_id: Union[str, int]) -> str:
        """
        Use this method to generate a new primary invite link for a
        chat; any previously generated primary link is revoked. The
        bot must be an administrator in the chat for this to work
        and must have the appropriate administrator rights. Returns
        the new invite link as String on success.

        Reference: https://core.telegram.org/bots/api#exportchatinvitelink

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :returns: str
        """
        return self(ExportChatInviteLink(chat_id=chat_id))

    def create_chat_invite_link(
        self,
        chat_id: Union[str, int],
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        creates_join_request: Optional[bool] = None,
    ) -> ChatInviteLink:
        """
        Use this method to create an additional invite link for a
        chat. The bot must be an administrator in the chat for this
        to work and must have the appropriate administrator rights.
        The link can be revoked using the method
        revokeChatInviteLink. Returns the new invite link as
        ChatInviteLink object.

        Reference: https://core.telegram.org/bots/api#createchatinvitelink

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param name: Invite link name; 0-32 characters
        :param expire_date: Point in time (Unix timestamp) when the link will expire
        :param member_limit: Maximum number of users that can be members of the chat
        simultaneously after joining the chat via this invite link;
        1-99999
        :param creates_join_request: True, if users joining the chat via the link need to be
        approved by chat administrators. If True, member_limit can't
        be specified
        :returns: ChatInviteLink
        """
        return self(
            CreateChatInviteLink(
                chat_id=chat_id,
                name=name,
                expire_date=expire_date,
                member_limit=member_limit,
                creates_join_request=creates_join_request,
            )
        )

    def edit_chat_invite_link(
        self,
        chat_id: Union[str, int],
        invite_link: str,
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        creates_join_request: Optional[bool] = None,
    ) -> ChatInviteLink:
        """
        Use this method to edit a non-primary invite link created by
        the bot. The bot must be an administrator in the chat for
        this to work and must have the appropriate administrator
        rights. Returns the edited invite link as a ChatInviteLink
        object.

        Reference: https://core.telegram.org/bots/api#editchatinvitelink

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param invite_link: The invite link to edit
        :param name: Invite link name; 0-32 characters
        :param expire_date: Point in time (Unix timestamp) when the link will expire
        :param member_limit: Maximum number of users that can be members of the chat
        simultaneously after joining the chat via this invite link;
        1-99999
        :param creates_join_request: True, if users joining the chat via the link need to be
        approved by chat administrators. If True, member_limit can't
        be specified
        :returns: ChatInviteLink
        """
        return self(
            EditChatInviteLink(
                chat_id=chat_id,
                invite_link=invite_link,
                name=name,
                expire_date=expire_date,
                member_limit=member_limit,
                creates_join_request=creates_join_request,
            )
        )

    def revoke_chat_invite_link(
        self, chat_id: Union[str, int], invite_link: str
    ) -> ChatInviteLink:
        """
        Use this method to revoke an invite link created by the bot.
        If the primary link is revoked, a new link is automatically
        generated. The bot must be an administrator in the chat for
        this to work and must have the appropriate administrator
        rights. Returns the revoked invite link as ChatInviteLink
        object.

        Reference: https://core.telegram.org/bots/api#revokechatinvitelink

        :param chat_id: Unique identifier of the target chat or username of the
        target channel (in the format @channelusername)
        :param invite_link: The invite link to revoke
        :returns: ChatInviteLink
        """
        return self(RevokeChatInviteLink(chat_id=chat_id, invite_link=invite_link))

    def approve_chat_join_request(self, chat_id: Union[str, int], user_id: int) -> bool:
        """
        Use this method to approve a chat join request. The bot must
        be an administrator in the chat for this to work and must
        have the can_invite_users administrator right. Returns True
        on success.

        Reference: https://core.telegram.org/bots/api#approvechatjoinrequest

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param user_id: Unique identifier of the target user
        :returns: bool
        """
        return self(ApproveChatJoinRequest(chat_id=chat_id, user_id=user_id))

    def decline_chat_join_request(self, chat_id: Union[str, int], user_id: int) -> bool:
        """
        Use this method to decline a chat join request. The bot must
        be an administrator in the chat for this to work and must
        have the can_invite_users administrator right. Returns True
        on success.

        Reference: https://core.telegram.org/bots/api#declinechatjoinrequest

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param user_id: Unique identifier of the target user
        :returns: bool
        """
        return self(DeclineChatJoinRequest(chat_id=chat_id, user_id=user_id))

    def set_chat_photo(self, chat_id: Union[str, int], photo: InputFile) -> bool:
        """
        Use this method to set a new profile photo for the chat.
        Photos can't be changed for private chats. The bot must be
        an administrator in the chat for this to work and must have
        the appropriate administrator rights. Returns True on
        success.

        Reference: https://core.telegram.org/bots/api#setchatphoto

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param photo: New chat photo, uploaded using multipart/form-data
        :returns: bool
        """
        return self(SetChatPhoto(chat_id=chat_id, photo=photo))

    def delete_chat_photo(self, chat_id: Union[str, int]) -> bool:
        """
        Use this method to delete a chat photo. Photos can't be
        changed for private chats. The bot must be an administrator
        in the chat for this to work and must have the appropriate
        administrator rights. Returns True on success.

        Reference: https://core.telegram.org/bots/api#deletechatphoto

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :returns: bool
        """
        return self(DeleteChatPhoto(chat_id=chat_id))

    def set_chat_title(self, chat_id: Union[str, int], title: str) -> bool:
        """
        Use this method to change the title of a chat. Titles can't
        be changed for private chats. The bot must be an
        administrator in the chat for this to work and must have the
        appropriate administrator rights. Returns True on success.

        Reference: https://core.telegram.org/bots/api#setchattitle

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param title: New chat title, 1-255 characters
        :returns: bool
        """
        return self(SetChatTitle(chat_id=chat_id, title=title))

    def set_chat_description(
        self, chat_id: Union[str, int], description: Optional[str] = None
    ) -> bool:
        """
        Use this method to change the description of a group, a
        supergroup or a channel. The bot must be an administrator in
        the chat for this to work and must have the appropriate
        administrator rights. Returns True on success.

        Reference: https://core.telegram.org/bots/api#setchatdescription

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param description: New chat description, 0-255 characters
        :returns: bool
        """
        return self(SetChatDescription(chat_id=chat_id, description=description))

    def pin_chat_message(
        self,
        chat_id: Union[str, int],
        message_id: int,
        disable_notification: Optional[bool] = None,
    ) -> bool:
        """
        Use this method to add a message to the list of pinned
        messages in a chat. If the chat is not a private chat, the
        bot must be an administrator in the chat for this to work
        and must have the 'can_pin_messages' administrator right in
        a supergroup or 'can_edit_messages' administrator right in a
        channel. Returns True on success.

        Reference: https://core.telegram.org/bots/api#pinchatmessage

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param message_id: Identifier of a message to pin
        :param disable_notification: Pass True, if it is not necessary to send a notification to
        all chat members about the new pinned message. Notifications
        are always disabled in channels and private chats.
        :returns: bool
        """
        return self(
            PinChatMessage(
                chat_id=chat_id,
                message_id=message_id,
                disable_notification=disable_notification,
            )
        )

    def unpin_chat_message(
        self, chat_id: Union[str, int], message_id: Optional[int] = None
    ) -> bool:
        """
        Use this method to remove a message from the list of pinned
        messages in a chat. If the chat is not a private chat, the
        bot must be an administrator in the chat for this to work
        and must have the 'can_pin_messages' administrator right in
        a supergroup or 'can_edit_messages' administrator right in a
        channel. Returns True on success.

        Reference: https://core.telegram.org/bots/api#unpinchatmessage

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param message_id: Identifier of a message to unpin. If not specified, the most
        recent pinned message (by sending date) will be unpinned.
        :returns: bool
        """
        return self(UnpinChatMessage(chat_id=chat_id, message_id=message_id))

    def unpin_all_chat_messages(self, chat_id: Union[str, int]) -> bool:
        """
        Use this method to clear the list of pinned messages in a
        chat. If the chat is not a private chat, the bot must be an
        administrator in the chat for this to work and must have the
        'can_pin_messages' administrator right in a supergroup or
        'can_edit_messages' administrator right in a channel.
        Returns True on success.

        Reference: https://core.telegram.org/bots/api#unpinallchatmessages

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :returns: bool
        """
        return self(UnpinAllChatMessages(chat_id=chat_id))

    def leave_chat(self, chat_id: Union[str, int]) -> bool:
        """
        Use this method for your bot to leave a group, supergroup or
        channel. Returns True on success.

        Reference: https://core.telegram.org/bots/api#leavechat

        :param chat_id: Unique identifier for the target chat or username of the
        target supergroup or channel (in the format
        @channelusername)
        :returns: bool
        """
        return self(LeaveChat(chat_id=chat_id))

    def get_chat(self, chat_id: Union[str, int]) -> ChatInfo:
        """
        Use this method to get up to date information about the chat
        (current name of the user for one-on-one conversations,
        current username of a user, group or channel, etc.). Returns
        a Chat object on success.

        Reference: https://core.telegram.org/bots/api#getchat

        :param chat_id: Unique identifier for the target chat or username of the
        target supergroup or channel (in the format
        @channelusername)
        :returns: ChatInfo
        """
        return self(GetChat(chat_id=chat_id))

    def get_chat_administrators(self, chat_id: Union[str, int]) -> List[ChatMember]:
        """
        Use this method to get a list of administrators in a chat.
        On success, returns an Array of ChatMember objects that
        contains information about all chat administrators except
        other bots. If the chat is a group or a supergroup and no
        administrators were appointed, only the creator will be
        returned.

        Reference: https://core.telegram.org/bots/api#getchatadministrators

        :param chat_id: Unique identifier for the target chat or username of the
        target supergroup or channel (in the format
        @channelusername)
        :returns: List[ChatMember]
        """
        return self(GetChatAdministrators(chat_id=chat_id))

    def get_chat_member_count(self, chat_id: Union[str, int]) -> int:
        """
        Use this method to get the number of members in a chat.
        Returns Int on success.

        Reference: https://core.telegram.org/bots/api#getchatmembercount

        :param chat_id: Unique identifier for the target chat or username of the
        target supergroup or channel (in the format
        @channelusername)
        :returns: int
        """
        return self(GetChatMemberCount(chat_id=chat_id))

    def get_chat_member(self, chat_id: Union[str, int], user_id: int) -> ChatMember:
        """
        Use this method to get information about a member of a chat.
        Returns a ChatMember object on success.

        Reference: https://core.telegram.org/bots/api#getchatmember

        :param chat_id: Unique identifier for the target chat or username of the
        target supergroup or channel (in the format
        @channelusername)
        :param user_id: Unique identifier of the target user
        :returns: ChatMember
        """
        return self(GetChatMember(chat_id=chat_id, user_id=user_id))

    def set_chat_sticker_set(
        self, chat_id: Union[str, int], sticker_set_name: str
    ) -> bool:
        """
        Use this method to set a new group sticker set for a
        supergroup. The bot must be an administrator in the chat for
        this to work and must have the appropriate administrator
        rights. Use the field can_set_sticker_set optionally
        returned in getChat requests to check if the bot can use
        this method. Returns True on success.

        Reference: https://core.telegram.org/bots/api#setchatstickerset

        :param chat_id: Unique identifier for the target chat or username of the
        target supergroup (in the format @supergroupusername)
        :param sticker_set_name: Name of the sticker set to be set as the group sticker set
        :returns: bool
        """
        return self(
            SetChatStickerSet(chat_id=chat_id, sticker_set_name=sticker_set_name)
        )

    def delete_chat_sticker_set(self, chat_id: Union[str, int]) -> bool:
        """
        Use this method to delete a group sticker set from a
        supergroup. The bot must be an administrator in the chat for
        this to work and must have the appropriate administrator
        rights. Use the field can_set_sticker_set optionally
        returned in getChat requests to check if the bot can use
        this method. Returns True on success.

        Reference: https://core.telegram.org/bots/api#deletechatstickerset

        :param chat_id: Unique identifier for the target chat or username of the
        target supergroup (in the format @supergroupusername)
        :returns: bool
        """
        return self(DeleteChatStickerSet(chat_id=chat_id))

    def answer_callback_query(
        self,
        callback_query_id: str,
        text: Optional[str] = None,
        show_alert: Optional[bool] = None,
        url: Optional[str] = None,
        cache_time: Optional[int] = None,
    ) -> bool:
        """
        Use this method to send answers to callback queries sent
        from inline keyboards. The answer will be displayed to the
        user as a notification at the top of the chat screen or as
        an alert. On success, True is returned.

        Reference: https://core.telegram.org/bots/api#answercallbackquery

        :param callback_query_id: Unique identifier for the query to be answered
        :param text: Text of the notification. If not specified, nothing will be
        shown to the user, 0-200 characters
        :param show_alert: If True, an alert will be shown by the client instead of a
        notification at the top of the chat screen. Defaults to
        false.
        :param url: URL that will be opened by the user's client. If you have
        created a Game and accepted the conditions via @Botfather,
        specify the URL that opens your game — note that this will
        only work if the query comes from a callback_game
        button.Otherwise, you may use links like
        t.me/your_bot?start=XXXX that open your bot with a
        parameter.
        :param cache_time: The maximum amount of time in seconds that the result of the
        callback query may be cached client-side. Telegram apps will
        support caching starting in version 3.14. Defaults to 0.
        :returns: bool
        """
        return self(
            AnswerCallbackQuery(
                callback_query_id=callback_query_id,
                text=text,
                show_alert=show_alert,
                url=url,
                cache_time=cache_time,
            )
        )

    def set_my_commands(
        self,
        commands: List[BotCommand],
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None,
    ) -> bool:
        """
        Use this method to change the list of the bot's commands.
        See https://core.telegram.org/bots#commands for more details
        about bot commands. Returns True on success.

        Reference: https://core.telegram.org/bots/api#setmycommands

        :param commands: A JSON-serialized list of bot commands to be set as the list
        of the bot's commands. At most 100 commands can be
        specified.
        :param scope: A JSON-serialized object, describing scope of users for
        which the commands are relevant. Defaults to
        BotCommandScopeDefault.
        :param language_code: A two-letter ISO 639-1 language code. If empty, commands
        will be applied to all users from the given scope, for whose
        language there are no dedicated commands
        :returns: bool
        """
        return self(
            SetMyCommands(commands=commands, scope=scope, language_code=language_code)
        )

    def delete_my_commands(
        self,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None,
    ) -> bool:
        """
        Use this method to delete the list of the bot's commands for
        the given scope and user language. After deletion, higher
        level commands will be shown to affected users. Returns True
        on success.

        Reference: https://core.telegram.org/bots/api#deletemycommands

        :param scope: A JSON-serialized object, describing scope of users for
        which the commands are relevant. Defaults to
        BotCommandScopeDefault.
        :param language_code: A two-letter ISO 639-1 language code. If empty, commands
        will be applied to all users from the given scope, for whose
        language there are no dedicated commands
        :returns: bool
        """
        return self(DeleteMyCommands(scope=scope, language_code=language_code))

    def get_my_commands(
        self,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None,
    ) -> List[BotCommand]:
        """
        Use this method to get the current list of the bot's
        commands for the given scope and user language. Returns
        Array of BotCommand on success. If commands aren't set, an
        empty list is returned.

        Reference: https://core.telegram.org/bots/api#getmycommands

        :param scope: A JSON-serialized object, describing scope of users.
        Defaults to BotCommandScopeDefault.
        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :returns: List[BotCommand]
        """
        return self(GetMyCommands(scope=scope, language_code=language_code))

    def edit_message_text(
        self,
        text: str,
        chat_id: Optional[Union[str, int]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        parse_mode: Optional[str] = None,
        entities: Optional[List[MessageEntity]] = None,
        disable_web_page_preview: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Union[Message, bool]:
        """
        Use this method to edit text and game messages. On success,
        if the edited message is not an inline message, the edited
        Message is returned, otherwise True is returned.

        Reference: https://core.telegram.org/bots/api#editmessagetext

        :param text: New text of the message, 1-4096 characters after entities
        parsing
        :param chat_id: Required if inline_message_id is not specified. Unique
        identifier for the target chat or username of the target
        channel (in the format @channelusername)
        :param message_id: Required if inline_message_id is not specified. Identifier
        of the message to edit
        :param inline_message_id: Required if chat_id and message_id are not specified.
        Identifier of the inline message
        :param parse_mode: Mode for parsing entities in the message text. See
        formatting options for more details.
        :param entities: A JSON-serialized list of special entities that appear in
        message text, which can be specified instead of parse_mode
        :param disable_web_page_preview: Disables link previews for links in this message
        :param reply_markup: A JSON-serialized object for an inline keyboard.
        :returns: Union[Message, bool]
        """
        return self(
            EditMessageText(
                text=text,
                chat_id=chat_id,
                message_id=message_id,
                inline_message_id=inline_message_id,
                parse_mode=parse_mode,
                entities=entities,
                disable_web_page_preview=disable_web_page_preview,
                reply_markup=reply_markup,
            )
        )

    def edit_message_caption(
        self,
        chat_id: Optional[Union[str, int]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Union[Message, bool]:
        """
        Use this method to edit captions of messages. On success, if
        the edited message is not an inline message, the edited
        Message is returned, otherwise True is returned.

        Reference: https://core.telegram.org/bots/api#editmessagecaption

        :param chat_id: Required if inline_message_id is not specified. Unique
        identifier for the target chat or username of the target
        channel (in the format @channelusername)
        :param message_id: Required if inline_message_id is not specified. Identifier
        of the message to edit
        :param inline_message_id: Required if chat_id and message_id are not specified.
        Identifier of the inline message
        :param caption: New caption of the message, 0-1024 characters after entities
        parsing
        :param parse_mode: Mode for parsing entities in the message caption. See
        formatting options for more details.
        :param caption_entities: A JSON-serialized list of special entities that appear in
        the caption, which can be specified instead of parse_mode
        :param reply_markup: A JSON-serialized object for an inline keyboard.
        :returns: Union[Message, bool]
        """
        return self(
            EditMessageCaption(
                chat_id=chat_id,
                message_id=message_id,
                inline_message_id=inline_message_id,
                caption=caption,
                parse_mode=parse_mode,
                caption_entities=caption_entities,
                reply_markup=reply_markup,
            )
        )

    def edit_message_media(
        self,
        media: InputMedia,
        chat_id: Optional[Union[str, int]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Union[Message, bool]:
        """
        Use this method to edit animation, audio, document, photo,
        or video messages. If a message is part of a message album,
        then it can be edited only to an audio for audio albums,
        only to a document for document albums and to a photo or a
        video otherwise. When an inline message is edited, a new
        file can't be uploaded; use a previously uploaded file via
        its file_id or specify a URL. On success, if the edited
        message is not an inline message, the edited Message is
        returned, otherwise True is returned.

        Reference: https://core.telegram.org/bots/api#editmessagemedia

        :param media: A JSON-serialized object for a new media content of the
        message
        :param chat_id: Required if inline_message_id is not specified. Unique
        identifier for the target chat or username of the target
        channel (in the format @channelusername)
        :param message_id: Required if inline_message_id is not specified. Identifier
        of the message to edit
        :param inline_message_id: Required if chat_id and message_id are not specified.
        Identifier of the inline message
        :param reply_markup: A JSON-serialized object for a new inline keyboard.
        :returns: Union[Message, bool]
        """
        return self(
            EditMessageMedia(
                media=media,
                chat_id=chat_id,
                message_id=message_id,
                inline_message_id=inline_message_id,
                reply_markup=reply_markup,
            )
        )

    def edit_message_reply_markup(
        self,
        chat_id: Optional[Union[str, int]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Union[Message, bool]:
        """
        Use this method to edit only the reply markup of messages.
        On success, if the edited message is not an inline message,
        the edited Message is returned, otherwise True is returned.

        Reference: https://core.telegram.org/bots/api#editmessagereplymarkup

        :param chat_id: Required if inline_message_id is not specified. Unique
        identifier for the target chat or username of the target
        channel (in the format @channelusername)
        :param message_id: Required if inline_message_id is not specified. Identifier
        of the message to edit
        :param inline_message_id: Required if chat_id and message_id are not specified.
        Identifier of the inline message
        :param reply_markup: A JSON-serialized object for an inline keyboard.
        :returns: Union[Message, bool]
        """
        return self(
            EditMessageReplyMarkup(
                chat_id=chat_id,
                message_id=message_id,
                inline_message_id=inline_message_id,
                reply_markup=reply_markup,
            )
        )

    def stop_poll(
        self,
        chat_id: Union[str, int],
        message_id: int,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Poll:
        """
        Use this method to stop a poll which was sent by the bot. On
        success, the stopped Poll is returned.

        Reference: https://core.telegram.org/bots/api#stoppoll

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param message_id: Identifier of the original message with the poll
        :param reply_markup: A JSON-serialized object for a new message inline keyboard.
        :returns: Poll
        """
        return self(
            StopPoll(chat_id=chat_id, message_id=message_id, reply_markup=reply_markup)
        )

    def delete_message(self, chat_id: Union[str, int], message_id: int) -> bool:
        """
        Use this method to delete a message, including service
        messages, with the following limitations:- A message can
        only be deleted if it was sent less than 48 hours ago.- A
        dice message in a private chat can only be deleted if it was
        sent more than 24 hours ago.- Bots can delete outgoing
        messages in private chats, groups, and supergroups.- Bots
        can delete incoming messages in private chats.- Bots granted
        can_post_messages permissions can delete outgoing messages
        in channels.- If the bot is an administrator of a group, it
        can delete any message there.- If the bot has
        can_delete_messages permission in a supergroup or a channel,
        it can delete any message there.Returns True on success.

        Reference: https://core.telegram.org/bots/api#deletemessage

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param message_id: Identifier of the message to delete
        :returns: bool
        """
        return self(DeleteMessage(chat_id=chat_id, message_id=message_id))

    def send_sticker(
        self,
        chat_id: Union[str, int],
        sticker: Union[InputFile, str],
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> Message:
        """
        Use this method to send static .WEBP, animated .TGS, or
        video .WEBM stickers. On success, the sent Message is
        returned.

        Reference: https://core.telegram.org/bots/api#sendsticker

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param sticker: Sticker to send. Pass a file_id as String to send a file
        that exists on the Telegram servers (recommended), pass an
        HTTP URL as a String for Telegram to get a .WEBP file from
        the Internet, or upload a new one using multipart/form-data.
        More info on Sending Files »
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for
        an inline keyboard, custom reply keyboard, instructions to
        remove reply keyboard or to force a reply from the user.
        :returns: Message
        """
        return self(
            SendSticker(
                chat_id=chat_id,
                sticker=sticker,
                disable_notification=disable_notification,
                protect_content=protect_content,
                reply_to_message_id=reply_to_message_id,
                allow_sending_without_reply=allow_sending_without_reply,
                reply_markup=reply_markup,
            )
        )

    def get_sticker_set(self, name: str) -> StickerSet:
        """
        Use this method to get a sticker set. On success, a
        StickerSet object is returned.

        Reference: https://core.telegram.org/bots/api#getstickerset

        :param name: Name of the sticker set
        :returns: StickerSet
        """
        return self(GetStickerSet(name=name))

    def upload_sticker_file(self, user_id: int, png_sticker: InputFile) -> File:
        """
        Use this method to upload a .PNG file with a sticker for
        later use in createNewStickerSet and addStickerToSet methods
        (can be used multiple times). Returns the uploaded File on
        success.

        Reference: https://core.telegram.org/bots/api#uploadstickerfile

        :param user_id: User identifier of sticker file owner
        :param png_sticker: PNG image with the sticker, must be up to 512 kilobytes in
        size, dimensions must not exceed 512px, and either width or
        height must be exactly 512px. More info on Sending Files »
        :returns: File
        """
        return self(UploadStickerFile(user_id=user_id, png_sticker=png_sticker))

    def create_new_sticker_set(
        self,
        user_id: int,
        name: str,
        title: str,
        emojis: str,
        png_sticker: Optional[Union[InputFile, str]] = None,
        tgs_sticker: Optional[InputFile] = None,
        webm_sticker: Optional[InputFile] = None,
        contains_masks: Optional[bool] = None,
        mask_position: Optional[MaskPosition] = None,
    ) -> bool:
        """
        Use this method to create a new sticker set owned by a user.
        The bot will be able to edit the sticker set thus created.
        You must use exactly one of the fields png_sticker,
        tgs_sticker, or webm_sticker. Returns True on success.

        Reference: https://core.telegram.org/bots/api#createnewstickerset

        :param user_id: User identifier of created sticker set owner
        :param name: Short name of sticker set, to be used in t.me/addstickers/
        URLs (e.g., animals). Can contain only english letters,
        digits and underscores. Must begin with a letter, can't
        contain consecutive underscores and must end in “_by_<bot
        username>”. <bot_username> is case insensitive. 1-64
        characters.
        :param title: Sticker set title, 1-64 characters
        :param emojis: One or more emoji corresponding to the sticker
        :param png_sticker: PNG image with the sticker, must be up to 512 kilobytes in
        size, dimensions must not exceed 512px, and either width or
        height must be exactly 512px. Pass a file_id as a String to
        send a file that already exists on the Telegram servers,
        pass an HTTP URL as a String for Telegram to get a file from
        the Internet, or upload a new one using multipart/form-data.
        More info on Sending Files »
        :param tgs_sticker: TGS animation with the sticker, uploaded using
        multipart/form-data. See
        https://core.telegram.org/stickers#animated-sticker-
        requirements for technical requirements
        :param webm_sticker: WEBM video with the sticker, uploaded using multipart/form-
        data. See https://core.telegram.org/stickers#video-sticker-
        requirements for technical requirements
        :param contains_masks: Pass True, if a set of mask stickers should be created
        :param mask_position: A JSON-serialized object for position where the mask should
        be placed on faces
        :returns: bool
        """
        return self(
            CreateNewStickerSet(
                user_id=user_id,
                name=name,
                title=title,
                emojis=emojis,
                png_sticker=png_sticker,
                tgs_sticker=tgs_sticker,
                webm_sticker=webm_sticker,
                contains_masks=contains_masks,
                mask_position=mask_position,
            )
        )

    def add_sticker_to_set(
        self,
        user_id: int,
        name: str,
        emojis: str,
        png_sticker: Optional[Union[InputFile, str]] = None,
        tgs_sticker: Optional[InputFile] = None,
        webm_sticker: Optional[InputFile] = None,
        mask_position: Optional[MaskPosition] = None,
    ) -> bool:
        """
        Use this method to add a new sticker to a set created by the
        bot. You must use exactly one of the fields png_sticker,
        tgs_sticker, or webm_sticker. Animated stickers can be added
        to animated sticker sets and only to them. Animated sticker
        sets can have up to 50 stickers. Static sticker sets can
        have up to 120 stickers. Returns True on success.

        Reference: https://core.telegram.org/bots/api#addstickertoset

        :param user_id: User identifier of sticker set owner
        :param name: Sticker set name
        :param emojis: One or more emoji corresponding to the sticker
        :param png_sticker: PNG image with the sticker, must be up to 512 kilobytes in
        size, dimensions must not exceed 512px, and either width or
        height must be exactly 512px. Pass a file_id as a String to
        send a file that already exists on the Telegram servers,
        pass an HTTP URL as a String for Telegram to get a file from
        the Internet, or upload a new one using multipart/form-data.
        More info on Sending Files »
        :param tgs_sticker: TGS animation with the sticker, uploaded using
        multipart/form-data. See
        https://core.telegram.org/stickers#animated-sticker-
        requirements for technical requirements
        :param webm_sticker: WEBM video with the sticker, uploaded using multipart/form-
        data. See https://core.telegram.org/stickers#video-sticker-
        requirements for technical requirements
        :param mask_position: A JSON-serialized object for position where the mask should
        be placed on faces
        :returns: bool
        """
        return self(
            AddStickerToSet(
                user_id=user_id,
                name=name,
                emojis=emojis,
                png_sticker=png_sticker,
                tgs_sticker=tgs_sticker,
                webm_sticker=webm_sticker,
                mask_position=mask_position,
            )
        )

    def set_sticker_position_in_set(self, sticker: str, position: int) -> bool:
        """
        Use this method to move a sticker in a set created by the
        bot to a specific position. Returns True on success.

        Reference: https://core.telegram.org/bots/api#setstickerpositioninset

        :param sticker: File identifier of the sticker
        :param position: New sticker position in the set, zero-based
        :returns: bool
        """
        return self(SetStickerPositionInSet(sticker=sticker, position=position))

    def delete_sticker_from_set(self, sticker: str) -> bool:
        """
        Use this method to delete a sticker from a set created by
        the bot. Returns True on success.

        Reference: https://core.telegram.org/bots/api#deletestickerfromset

        :param sticker: File identifier of the sticker
        :returns: bool
        """
        return self(DeleteStickerFromSet(sticker=sticker))

    def set_sticker_set_thumb(
        self, name: str, user_id: int, thumb: Optional[Union[InputFile, str]] = None
    ) -> bool:
        """
        Use this method to set the thumbnail of a sticker set.
        Animated thumbnails can be set for animated sticker sets
        only. Video thumbnails can be set only for video sticker
        sets only. Returns True on success.

        Reference: https://core.telegram.org/bots/api#setstickersetthumb

        :param name: Sticker set name
        :param user_id: User identifier of the sticker set owner
        :param thumb: A PNG image with the thumbnail, must be up to 128 kilobytes
        in size and have width and height exactly 100px, or a TGS
        animation with the thumbnail up to 32 kilobytes in size; see
        https://core.telegram.org/stickers#animated-sticker-
        requirements for animated sticker technical requirements, or
        a WEBM video with the thumbnail up to 32 kilobytes in size;
        see https://core.telegram.org/stickers#video-sticker-
        requirements for video sticker technical requirements. Pass
        a file_id as a String to send a file that already exists on
        the Telegram servers, pass an HTTP URL as a String for
        Telegram to get a file from the Internet, or upload a new
        one using multipart/form-data. More info on Sending Files ».
        Animated sticker set thumbnails can't be uploaded via HTTP
        URL.
        :returns: bool
        """
        return self(SetStickerSetThumb(name=name, user_id=user_id, thumb=thumb))

    def answer_inline_query(
        self,
        inline_query_id: str,
        results: List[InlineQueryResult],
        cache_time: Optional[int] = None,
        is_personal: Optional[bool] = None,
        next_offset: Optional[str] = None,
        switch_pm_text: Optional[str] = None,
        switch_pm_parameter: Optional[str] = None,
    ) -> bool:
        """
        Use this method to send answers to an inline query. On
        success, True is returned.No more than 50 results per query
        are allowed.

        Reference: https://core.telegram.org/bots/api#answerinlinequery

        :param inline_query_id: Unique identifier for the answered query
        :param results: A JSON-serialized array of results for the inline query
        :param cache_time: The maximum amount of time in seconds that the result of the
        inline query may be cached on the server. Defaults to 300.
        :param is_personal: Pass True, if results may be cached on the server side only
        for the user that sent the query. By default, results may be
        returned to any user who sends the same query
        :param next_offset: Pass the offset that a client should send in the next query
        with the same text to receive more results. Pass an empty
        string if there are no more results or if you don't support
        pagination. Offset length can't exceed 64 bytes.
        :param switch_pm_text: If passed, clients will display a button with specified text
        that switches the user to a private chat with the bot and
        sends the bot a start message with the parameter
        switch_pm_parameter
        :param switch_pm_parameter: Deep-linking parameter for the /start message sent to the
        bot when user presses the switch button. 1-64 characters,
        only A-Z, a-z, 0-9, _ and - are allowed.Example: An inline
        bot that sends YouTube videos can ask the user to connect
        the bot to their YouTube account to adapt search results
        accordingly. To do this, it displays a 'Connect your YouTube
        account' button above the results, or even before showing
        any. The user presses the button, switches to a private chat
        with the bot and, in doing so, passes a start parameter that
        instructs the bot to return an OAuth link. Once done, the
        bot can offer a switch_inline button so that the user can
        easily return to the chat where they wanted to use the bot's
        inline capabilities.
        :returns: bool
        """
        return self(
            AnswerInlineQuery(
                inline_query_id=inline_query_id,
                results=results,
                cache_time=cache_time,
                is_personal=is_personal,
                next_offset=next_offset,
                switch_pm_text=switch_pm_text,
                switch_pm_parameter=switch_pm_parameter,
            )
        )

    def send_invoice(
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
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Message:
        """
        Use this method to send invoices. On success, the sent
        Message is returned.

        Reference: https://core.telegram.org/bots/api#sendinvoice

        :param chat_id: Unique identifier for the target chat or username of the
        target channel (in the format @channelusername)
        :param title: Product name, 1-32 characters
        :param description: Product description, 1-255 characters
        :param payload: Bot-defined invoice payload, 1-128 bytes. This will not be
        displayed to the user, use for your internal processes.
        :param provider_token: Payments provider token, obtained via Botfather
        :param currency: Three-letter ISO 4217 currency code, see more on currencies
        :param prices: Price breakdown, a JSON-serialized list of components (e.g.
        product price, tax, discount, delivery cost, delivery tax,
        bonus, etc.)
        :param max_tip_amount: The maximum accepted amount for tips in the smallest units
        of the currency (integer, not float/double). For example,
        for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See
        the exp parameter in currencies.json, it shows the number of
        digits past the decimal point for each currency (2 for the
        majority of currencies). Defaults to 0
        :param suggested_tip_amounts: A JSON-serialized array of suggested amounts of tips in the
        smallest units of the currency (integer, not float/double).
        At most 4 suggested tip amounts can be specified. The
        suggested tip amounts must be positive, passed in a strictly
        increased order and must not exceed max_tip_amount.
        :param start_parameter: Unique deep-linking parameter. If left empty, forwarded
        copies of the sent message will have a Pay button, allowing
        multiple users to pay directly from the forwarded message,
        using the same invoice. If non-empty, forwarded copies of
        the sent message will have a URL button with a deep link to
        the bot (instead of a Pay button), with the value used as
        the start parameter
        :param provider_data: A JSON-serialized data about the invoice, which will be
        shared with the payment provider. A detailed description of
        required fields should be provided by the payment provider.
        :param photo_url: URL of the product photo for the invoice. Can be a photo of
        the goods or a marketing image for a service. People like it
        better when they see what they are paying for.
        :param photo_size: Photo size
        :param photo_width: Photo width
        :param photo_height: Photo height
        :param need_name: Pass True, if you require the user's full name to complete
        the order
        :param need_phone_number: Pass True, if you require the user's phone number to
        complete the order
        :param need_email: Pass True, if you require the user's email address to
        complete the order
        :param need_shipping_address: Pass True, if you require the user's shipping address to
        complete the order
        :param send_phone_number_to_provider: Pass True, if user's phone number should be sent to provider
        :param send_email_to_provider: Pass True, if user's email address should be sent to
        provider
        :param is_flexible: Pass True, if the final price depends on the shipping method
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: A JSON-serialized object for an inline keyboard. If empty,
        one 'Pay total price' button will be shown. If not empty,
        the first button must be a Pay button.
        :returns: Message
        """
        return self(
            SendInvoice(
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
                reply_markup=reply_markup,
            )
        )

    def answer_shipping_query(
        self,
        shipping_query_id: str,
        ok: bool,
        shipping_options: Optional[List[ShippingOption]] = None,
        error_message: Optional[str] = None,
    ) -> bool:
        """
        If you sent an invoice requesting a shipping address and the
        parameter is_flexible was specified, the Bot API will send
        an Update with a shipping_query field to the bot. Use this
        method to reply to shipping queries. On success, True is
        returned.

        Reference: https://core.telegram.org/bots/api#answershippingquery

        :param shipping_query_id: Unique identifier for the query to be answered
        :param ok: Specify True if delivery to the specified address is
        possible and False if there are any problems (for example,
        if delivery to the specified address is not possible)
        :param shipping_options: Required if ok is True. A JSON-serialized array of available
        shipping options.
        :param error_message: Required if ok is False. Error message in human readable
        form that explains why it is impossible to complete the
        order (e.g. "Sorry, delivery to your desired address is
        unavailable'). Telegram will display this message to the
        user.
        :returns: bool
        """
        return self(
            AnswerShippingQuery(
                shipping_query_id=shipping_query_id,
                ok=ok,
                shipping_options=shipping_options,
                error_message=error_message,
            )
        )

    def answer_pre_checkout_query(
        self, pre_checkout_query_id: str, ok: bool, error_message: Optional[str] = None
    ) -> bool:
        """
        Once the user has confirmed their payment and shipping
        details, the Bot API sends the final confirmation in the
        form of an Update with the field pre_checkout_query. Use
        this method to respond to such pre-checkout queries. On
        success, True is returned. Note: The Bot API must receive an
        answer within 10 seconds after the pre-checkout query was
        sent.

        Reference: https://core.telegram.org/bots/api#answerprecheckoutquery

        :param pre_checkout_query_id: Unique identifier for the query to be answered
        :param ok: Specify True if everything is alright (goods are available,
        etc.) and the bot is ready to proceed with the order. Use
        False if there are any problems.
        :param error_message: Required if ok is False. Error message in human readable
        form that explains the reason for failure to proceed with
        the checkout (e.g. "Sorry, somebody just bought the last of
        our amazing black T-shirts while you were busy filling out
        your payment details. Please choose a different color or
        garment!"). Telegram will display this message to the user.
        :returns: bool
        """
        return self(
            AnswerPreCheckoutQuery(
                pre_checkout_query_id=pre_checkout_query_id,
                ok=ok,
                error_message=error_message,
            )
        )

    def set_passport_data_errors(
        self, user_id: int, errors: List[PassportElementError]
    ) -> bool:
        """
        Informs a user that some of the Telegram Passport elements
        they provided contains errors. The user will not be able to
        re-submit their Passport to you until the errors are fixed
        (the contents of the field for which you returned the error
        must change). Returns True on success.

        Reference: https://core.telegram.org/bots/api#setpassportdataerrors

        :param user_id: User identifier
        :param errors: A JSON-serialized array describing the errors
        :returns: bool
        """
        return self(SetPassportDataErrors(user_id=user_id, errors=errors))

    def send_game(
        self,
        chat_id: int,
        game_short_name: str,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Message:
        """
        Use this method to send a game. On success, the sent Message
        is returned.

        Reference: https://core.telegram.org/bots/api#sendgame

        :param chat_id: Unique identifier for the target chat
        :param game_short_name: Short name of the game, serves as the unique identifier for
        the game. Set up your games via Botfather.
        :param disable_notification: Sends the message silently. Users will receive a
        notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding
        and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the
        specified replied-to message is not found
        :param reply_markup: A JSON-serialized object for an inline keyboard. If empty,
        one 'Play game_title' button will be shown. If not empty,
        the first button must launch the game.
        :returns: Message
        """
        return self(
            SendGame(
                chat_id=chat_id,
                game_short_name=game_short_name,
                disable_notification=disable_notification,
                protect_content=protect_content,
                reply_to_message_id=reply_to_message_id,
                allow_sending_without_reply=allow_sending_without_reply,
                reply_markup=reply_markup,
            )
        )

    def set_game_score(
        self,
        user_id: int,
        score: int,
        force: Optional[bool] = None,
        disable_edit_message: Optional[bool] = None,
        chat_id: Optional[int] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
    ) -> Union[Message, bool]:
        """
        Use this method to set the score of the specified user in a
        game message. On success, if the message is not an inline
        message, the Message is returned, otherwise True is
        returned. Returns an error, if the new score is not greater
        than the user's current score in the chat and force is
        False.

        Reference: https://core.telegram.org/bots/api#setgamescore

        :param user_id: User identifier
        :param score: New score, must be non-negative
        :param force: Pass True, if the high score is allowed to decrease. This
        can be useful when fixing mistakes or banning cheaters
        :param disable_edit_message: Pass True, if the game message should not be automatically
        edited to include the current scoreboard
        :param chat_id: Required if inline_message_id is not specified. Unique
        identifier for the target chat
        :param message_id: Required if inline_message_id is not specified. Identifier
        of the sent message
        :param inline_message_id: Required if chat_id and message_id are not specified.
        Identifier of the inline message
        :returns: Union[Message, bool]
        """
        return self(
            SetGameScore(
                user_id=user_id,
                score=score,
                force=force,
                disable_edit_message=disable_edit_message,
                chat_id=chat_id,
                message_id=message_id,
                inline_message_id=inline_message_id,
            )
        )

    def get_game_high_scores(
        self,
        user_id: int,
        chat_id: Optional[int] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
    ) -> List[GameHighScore]:
        """
        Use this method to get data for high score tables. Will
        return the score of the specified user and several of their
        neighbors in a game. On success, returns an Array of
        GameHighScore objects.

        Reference: https://core.telegram.org/bots/api#getgamehighscores

        :param user_id: Target user id
        :param chat_id: Required if inline_message_id is not specified. Unique
        identifier for the target chat
        :param message_id: Required if inline_message_id is not specified. Identifier
        of the sent message
        :param inline_message_id: Required if chat_id and message_id are not specified.
        Identifier of the inline message
        :returns: List[GameHighScore]
        """
        return self(
            GetGameHighScores(
                user_id=user_id,
                chat_id=chat_id,
                message_id=message_id,
                inline_message_id=inline_message_id,
            )
        )
