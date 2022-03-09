from dataclasses import dataclass
from typing import Optional

from ..client.bot import Bot


@dataclass
class TelegramTypeEvent:
    _bot: Optional[Bot] = None

    @property
    def bot(self):
        return self._bot

    @bot.setter
    def bot(self, _bot):
        self._bot = _bot
