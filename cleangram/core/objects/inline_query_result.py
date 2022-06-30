from __future__ import annotations

from .base import TelegramObject


class InlineQueryResult(TelegramObject):
    """
    This object represents one result of an inline query. Telegram clients
    currently support results of the following 20 types:

        :class:`cleangram.InlineQueryResultCachedAudio`
        :class:`cleangram.InlineQueryResultCachedDocument`
        :class:`cleangram.InlineQueryResultCachedGif`
        :class:`cleangram.InlineQueryResultCachedMpeg4Gif`
        :class:`cleangram.InlineQueryResultCachedPhoto`
        :class:`cleangram.InlineQueryResultCachedSticker`
        :class:`cleangram.InlineQueryResultCachedVideo`
        :class:`cleangram.InlineQueryResultCachedVoice`
        :class:`cleangram.InlineQueryResultArticle`
        :class:`cleangram.InlineQueryResultAudio`
        :class:`cleangram.InlineQueryResultContact`
        :class:`cleangram.InlineQueryResultGame`
        :class:`cleangram.InlineQueryResultDocument`
        :class:`cleangram.InlineQueryResultGif`
        :class:`cleangram.InlineQueryResultLocation`
        :class:`cleangram.InlineQueryResultMpeg4Gif`
        :class:`cleangram.InlineQueryResultPhoto`
        :class:`cleangram.InlineQueryResultVenue`
        :class:`cleangram.InlineQueryResultVideo`
        :class:`cleangram.InlineQueryResultVoice`
    Note: All URLs passed in inline query results will be available to end
    users and therefore must be assumed to be public.

        :class:`cleangram.InlineQueryResultCachedAudio`
        :class:`cleangram.InlineQueryResultCachedDocument`
        :class:`cleangram.InlineQueryResultCachedGif`
        :class:`cleangram.InlineQueryResultCachedMpeg4Gif`
        :class:`cleangram.InlineQueryResultCachedPhoto`
        :class:`cleangram.InlineQueryResultCachedSticker`
        :class:`cleangram.InlineQueryResultCachedVideo`
        :class:`cleangram.InlineQueryResultCachedVoice`
        :class:`cleangram.InlineQueryResultArticle`
        :class:`cleangram.InlineQueryResultAudio`
        :class:`cleangram.InlineQueryResultContact`
        :class:`cleangram.InlineQueryResultGame`
        :class:`cleangram.InlineQueryResultDocument`
        :class:`cleangram.InlineQueryResultGif`
        :class:`cleangram.InlineQueryResultLocation`
        :class:`cleangram.InlineQueryResultMpeg4Gif`
        :class:`cleangram.InlineQueryResultPhoto`
        :class:`cleangram.InlineQueryResultVenue`
        :class:`cleangram.InlineQueryResultVideo`
        :class:`cleangram.InlineQueryResultVoice`

    Reference: https://core.telegram.org/bots/api#inlinequeryresult
    """
