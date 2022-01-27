from .._version import __version__
from ..core import __bot_api__


def get_info():
    return f"""Version:
    Cleangram: {__version__}
    Bot API: {__bot_api__}"""
