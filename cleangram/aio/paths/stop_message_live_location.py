from typing import Union

from ...core.objects.response import Response
from ...core.paths.stop_message_live_location import (
    StopMessageLiveLocation as _StopMessageLiveLocation,
)
from ..objects import Message


class StopMessageLiveLocation(
    _StopMessageLiveLocation, response=Response[Union[bool, Message]]
):
    """
    Use this method to stop updating a live location message before
    live_period expires. On success, if the message is not an inline
    message, the edited Message is returned, otherwise True is returned.

    Reference: https://core.telegram.org/bots/api#stopmessagelivelocation
    """
