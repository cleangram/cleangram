from dataclasses import dataclass
from typing import Optional


@dataclass
class InputFile:
    path: Optional[str] = None

    def __repr__(self):
        return f"InputFile({self.path!r})"

    def open(self):
        return open(self.path, "rb")
