from pathlib import Path
from typing import Union


class InputFile:
    def __init__(self, file: Union[str, bytes, Path]):
        self.file = file

    def __enter__(self):
        self._opened = open(self.file, "rb")
        return self._opened

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._opened.close()
