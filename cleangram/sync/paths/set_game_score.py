from typing import Union

from ...core.objects.response import Response
from ...core.paths.set_game_score import SetGameScore as _SetGameScore
from ..objects import Message


class SetGameScore(_SetGameScore, response=Response[Union[bool, Message]]):
    """
    Use this method to set the score of the specified user in a game
    message. On success, if the message is not an inline message, the
    Message is returned, otherwise True is returned. Returns an error, if
    the new score is not greater than the user's current score in the chat
    and force is False.

    Reference: https://core.telegram.org/bots/api#setgamescore
    """
