from typing import TypeVar, Optional

T = TypeVar("T")


def fit(original: Optional[T], base: Optional[T]) -> Optional[T]:
    if original is None:
        return base
    return original
