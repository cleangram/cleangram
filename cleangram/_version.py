major: int = 0
minor: int = 0
micro: int = 0
release: str = "a1"
__version__ = ".".join(map(str, [major, minor, micro, release]))
