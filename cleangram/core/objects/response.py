from typing import Generic, Optional, TypeVar

from pydantic.generics import GenericModel

from .response_parameters import ResponseParameters

T = TypeVar("T")


class Response(GenericModel, Generic[T]):
    ok: bool
    description: Optional[str] = None
    error_code: Optional[int] = None
    parameters: Optional[ResponseParameters] = None
    result: Optional[T] = None
