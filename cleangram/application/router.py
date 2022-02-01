from ..types import Message
from .observers.update import UpdateObserver


class Router:
    def __init__(self, **kwargs):
        self.message = UpdateObserver[Message]()

    async def notify(self, update, bot, raw=None, secret=None):
        ...
