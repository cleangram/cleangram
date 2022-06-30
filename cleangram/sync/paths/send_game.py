from ...core.objects.response import Response
from ...core.paths.send_game import SendGame as _SendGame
from ..objects import Message


class SendGame(_SendGame, response=Response[Message]):
    """
    Use this method to send a game. On success, the sent Message is
    returned.

    Reference: https://core.telegram.org/bots/api#sendgame
    """
