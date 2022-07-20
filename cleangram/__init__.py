from ._version import __version__, __bot_api__
from .core import *
from . import core, aio, sync

__all__ = [*core.__all__, "aio", "sync"]
