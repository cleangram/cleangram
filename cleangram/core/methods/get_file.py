from __future__ import annotations

from dataclasses import dataclass


from ..types import (
    Response,
    File
)
from .base import TelegramMethod


@dataclass
class GetFile(TelegramMethod, response=Response[File]):
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
    """

    file_id: str
    """File identifier to get info about"""
