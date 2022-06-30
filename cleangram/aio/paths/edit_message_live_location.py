from typing import Union

from ...core.objects.response import Response
from ...core.paths.edit_message_live_location import (
    EditMessageLiveLocation as _EditMessageLiveLocation,
)
from ..objects import Message


class EditMessageLiveLocation(
    _EditMessageLiveLocation, response=Response[Union[bool, Message]]
):
    """
    Use this method to edit live location messages. A location can be
    edited until its live_period expires or editing is explicitly disabled
    by a call to stopMessageLiveLocation. On success, if the edited
    message is not an inline message, the edited Message is returned,
    otherwise True is returned.

    Reference: https://core.telegram.org/bots/api#editmessagelivelocation
    """
