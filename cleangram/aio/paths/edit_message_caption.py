from typing import Union

from ...core.objects.response import Response
from ...core.paths.edit_message_caption import (
    EditMessageCaption as _EditMessageCaption,
)
from ..objects import Message


class EditMessageCaption(
    _EditMessageCaption, response=Response[Union[bool, Message]]
):
    """
    Use this method to edit captions of messages. On success, if the
    edited message is not an inline message, the edited Message is
    returned, otherwise True is returned.

    Reference: https://core.telegram.org/bots/api#editmessagecaption
    """
