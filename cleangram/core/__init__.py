from .paths import *
from .objects import *
from .bot.bot import Bot

from . import paths, objects

__all__ = [
    *paths.__all__,
    *objects.__all__,
    "Bot"
]
