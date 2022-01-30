from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, List

from ..types import (
    Response,
    InputFile
)
from .base import TelegramMethod


@dataclass
class SetWebhook(TelegramMethod, response=Response[bool]):
    """
    Use this method to specify a url and receive incoming
    updates via an outgoing webhook. Whenever there is an update
    for the bot, we will send an HTTPS POST request to the
    specified url, containing a JSON-serialized Update. In case
    of an unsuccessful request, we will give up after a
    reasonable amount of attempts. Returns True on success.

    Reference: https://core.telegram.org/bots/api#setwebhook
    """

    url: str
    """HTTPS url to send updates to. Use an empty string to remove
    webhook integration"""

    certificate: Optional[InputFile] = field(default=None)
    """Upload your public key certificate so that the root
    certificate in use can be checked. See our self-signed guide
    for details."""

    ip_address: Optional[str] = field(default=None)
    """The fixed IP address which will be used to send webhook
    requests instead of the IP address resolved through DNS"""

    max_connections: Optional[int] = field(default=None)
    """Maximum allowed number of simultaneous HTTPS connections to
    the webhook for update delivery, 1-100. Defaults to 40. Use
    lower values to limit the load on your bot's server, and
    higher values to increase your bot's throughput."""

    allowed_updates: Optional[List[str]] = field(default=None)
    """A JSON-serialized list of the update types you want your bot
    to receive. For example, specify [“message”,
    “edited_channel_post”, “callback_query”] to only receive
    updates of these types. See Update for a complete list of
    available update types. Specify an empty list to receive all
    update types except chat_member (default). If not specified,
    the previous setting will be used.Please note that this
    parameter doesn't affect updates created before the call to
    the setWebhook, so unwanted updates may be received for a
    short period of time."""

    drop_pending_updates: Optional[bool] = field(default=None)
    """Pass True to drop all pending updates"""
