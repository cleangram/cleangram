from typing import Union

from ...core.objects.response import Response
from ...core.paths.edit_message_text import EditMessageText as _EditMessageText
from ..objects import Message


class EditMessageText(
    _EditMessageText, response=Response[Union[bool, Message]]
):
    """
    Use this method to edit text and game messages. On success, if the
    edited message is not an inline message, the edited Message is
    returned, otherwise True is returned.

    Reference: https://core.telegram.org/bots/api#editmessagetext
    """
