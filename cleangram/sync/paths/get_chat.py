from ...core.objects.response import Response
from ...core.paths.get_chat import GetChat as _GetChat
from ..objects import Chat


class GetChat(_GetChat, response=Response[Chat]):
    """
    Use this method to get up to date information about the chat (current
    name of the user for one-on-one conversations, current username of a
    user, group or channel, etc.). Returns a Chat object on success.

    Reference: https://core.telegram.org/bots/api#getchat
    """
