from typing import Union

from ...core.objects.response import Response
from ...core.paths.edit_message_reply_markup import (
    EditMessageReplyMarkup as _EditMessageReplyMarkup,
)
from ..objects import Message


class EditMessageReplyMarkup(
    _EditMessageReplyMarkup, response=Response[Union[bool, Message]]
):
    """
    Use this method to edit only the reply markup of messages. On success,
    if the edited message is not an inline message, the edited Message is
    returned, otherwise True is returned.

    Reference: https://core.telegram.org/bots/api#editmessagereplymarkup
    """
