from dataclasses import dataclass
from typing import Dict

from ..types import InputFile


@dataclass
class Request:
    url: str
    data: dict
    files: Dict[str, InputFile]
    timeout: float
