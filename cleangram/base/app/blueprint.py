from ...base.types import Message
from .observers.update import UpdateObserver


class BaseBlueprint:
    message: UpdateObserver[Message]
    edited_message: UpdateObserver[Message]
