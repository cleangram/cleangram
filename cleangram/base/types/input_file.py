from pathlib import Path
from typing import Union


class InputFile:
    def __init__(self, path: Union[str, bytes, Path]):
        self.__path = path

    def __enter__(self):
        self.__file = open(self.__path, "rb")
        return self.__file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__file.close()
