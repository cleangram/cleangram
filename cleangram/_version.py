major: int = 0
minor: int = 0
micro: int = 0
release: str = "dev1"
__version__ = ".".join(map(str, [major, minor, micro, release]))
__bot_api__ = "5.7"
__doc__ = """
Cleangram - Telegram Bot API wrapper
"""
