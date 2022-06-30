from ...core.objects.response import Response
from ...core.paths.send_dice import SendDice as _SendDice
from ..objects import Message


class SendDice(_SendDice, response=Response[Message]):
    """
    Use this method to send an animated emoji that will display a random
    value. On success, the sent Message is returned.

    Reference: https://core.telegram.org/bots/api#senddice
    """
