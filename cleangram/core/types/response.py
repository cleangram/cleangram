from dataclasses import dataclass, field
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


@dataclass
class Response(Generic[T]):
    ok: bool
    result: Optional[T] = None
