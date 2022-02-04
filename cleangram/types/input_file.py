from pathlib import Path
from typing import Union


class InputFile:
    def __init__(self, file: Union[str, bytes, Path]):
        self.file = file
