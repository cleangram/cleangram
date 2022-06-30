from ...core.objects.response import Response
from ..objects import User
from .base import TelegramPath


class GetMe(TelegramPath, response=Response[User]):
    """
    A simple method for testing your bot's authentication token. Requires
    no parameters. Returns basic information about the bot in form of a
    User object.

    Reference: https://core.telegram.org/bots/api#getme
    """
