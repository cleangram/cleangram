from http import HTTPStatus

from dataclasses import dataclass, field
from typing import Optional, Dict

from .types import Response


class TelegramError(Exception):
    def __init__(self, response: Response):
        self.code: Optional[int] = response.error_code
        self.description: Optional[str] = response.description
        self.retry_after: Optional[int] = response.parameters.retry_after
        self.migrate_to_chat_id: Optional[int] = response.parameters.migrate_to_chat_id

    def __str__(self):
        return self.description


# HTTP errors
BadRequest = type("BadRequest", (TelegramError,), {})  # 400
Unauthorized = type("Unauthorized", (TelegramError,), {})  # 401
Forbidden = type("Forbidden", (TelegramError,), {})  # 403
NotFound = type("NotFound", (TelegramError,), {})  # 404
Conflict = type("Conflict", (TelegramError,), {})  # 409
TooManyRequests = type("TooManyRequests", (TelegramError,), {})  # 429


error_types: Dict[int, type] = {
    HTTPStatus.BAD_REQUEST: BadRequest,  # 400
    HTTPStatus.UNAUTHORIZED: Unauthorized,  # 401
    HTTPStatus.FORBIDDEN: Forbidden,  # 403
    HTTPStatus.NOT_FOUND: NotFound,  # 404
    HTTPStatus.CONFLICT: Conflict,  # 409
    HTTPStatus.TOO_MANY_REQUESTS: TooManyRequests,  # 429
}


def check(response: Response):
    if response.ok:
        return
    error: type = error_types.get(response.error_code or 0, TelegramError)
    raise error(response)
