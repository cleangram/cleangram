from __future__ import annotations

from dataclasses import dataclass


from ..types import Response
from .base import TelegramMethod


@dataclass
class Close(TelegramMethod, response=Response[bool]):
    """
    Use this method to close the bot instance before moving it
    from one local server to another. You need to delete the
    webhook before calling this method to ensure that the bot
    isn't launched again after server restart. The method will
    return error 429 in the first 10 minutes after the bot is
    launched. Returns True on success. Requires no parameters.

    Reference: https://core.telegram.org/bots/api#close
    """
