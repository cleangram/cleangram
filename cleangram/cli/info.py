from .._version import __version__
from ..telegram import __bot_api__


def get_info():
    print(f"""Version:
    Cleangram: {__version__}
    Bot API: {__bot_api__}""")
