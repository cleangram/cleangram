from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, List

from ..types import (
    Response,
    InlineQueryResult
)
from .base import TelegramMethod


@dataclass
class AnswerInlineQuery(TelegramMethod, response=Response[bool]):
    """
    Use this method to send answers to an inline query. On
    success, True is returned.No more than 50 results per query
    are allowed.

    Reference: https://core.telegram.org/bots/api#answerinlinequery
    """

    inline_query_id: str
    """Unique identifier for the answered query"""

    results: List[InlineQueryResult]
    """A JSON-serialized array of results for the inline query"""

    cache_time: Optional[int] = field(default=None)
    """The maximum amount of time in seconds that the result of the
    inline query may be cached on the server. Defaults to 300."""

    is_personal: Optional[bool] = field(default=None)
    """Pass True, if results may be cached on the server side only
    for the user that sent the query. By default, results may be
    returned to any user who sends the same query"""

    next_offset: Optional[str] = field(default=None)
    """Pass the offset that a client should send in the next query
    with the same text to receive more results. Pass an empty
    string if there are no more results or if you don't support
    pagination. Offset length can't exceed 64 bytes."""

    switch_pm_text: Optional[str] = field(default=None)
    """If passed, clients will display a button with specified text
    that switches the user to a private chat with the bot and
    sends the bot a start message with the parameter
    switch_pm_parameter"""

    switch_pm_parameter: Optional[str] = field(default=None)
    """Deep-linking parameter for the /start message sent to the
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
    inline capabilities."""
