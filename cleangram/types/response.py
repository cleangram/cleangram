from dataclasses import dataclass, field
from typing import Generic, TypeVar, Optional

from .response_parameters import ResponseParameters

T = TypeVar("T")


@dataclass(frozen=True)
class Response(Generic[T]):
    ok: bool
    description: Optional[str] = field(default=None)
    error_code: Optional[int] = field(default=None)
    parameters: Optional[ResponseParameters] = field(default_factory=ResponseParameters)
    result: Optional[T] = field(default=None)
