import secrets
from typing import Dict, Optional, Union

from ..types import InputFile


def attach(file: Optional[Union[InputFile, str]], files: Dict[str, InputFile]):
    if isinstance(file, InputFile):
        token = secrets.token_urlsafe(6)
        files[token] = file
        return f"attach://{token}"
    return file
