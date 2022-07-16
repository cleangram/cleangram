from __future__ import annotations

import abc
from typing import Optional


class Http(abc.ABC):
    @abc.abstractmethod
    def __call__(self, bot, path, timeout: Optional[float]):
        ...

    @abc.abstractmethod
    def close(self):
        ...
