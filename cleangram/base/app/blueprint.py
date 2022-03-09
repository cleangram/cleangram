from __future__ import annotations

import abc
import logging
from typing import List, Any, Dict, Optional

from .. import TelegramType
from ..app.observers import BaseHandlerObserver
from ..types import Update


class BaseBlueprint(abc.ABC):
    def __init__(
        self,
        name: str,
        *filters,
        children: List[BaseBlueprint] = (),
        parent: Optional[BaseBlueprint] = None,
        deps: Dict[str, Any] = None,
        flags: Dict[str, Any] = None,
        **kwargs
    ) -> None:
        self._name = name
        self._filters = filters
        self._parent = parent
        self._children = children
        self._deps = deps or {}
        self._flags = flags or {}
        self._handler_observers = {
            name: obs for name, obs in vars(self).items()
            if isinstance(obs, BaseHandlerObserver)
        }

    @property
    def name(self):
        return self._name

    @property
    def children(self):
        return self._children

    @property
    def parent(self) -> BaseBlueprint:
        return self._parent

    @parent.setter
    def parent(self, _parent):
        self._parent = _parent

    @property
    def deps(self):
        return self._deps

    @property
    def root(self) -> BaseBlueprint:
        _root = self
        while parent := _root.parent:
            _root = parent
        return _root

    @property
    def log(self):
        if parent := self._parent:
            return parent.log.getChild(self._name)
        else:
            return logging.getLogger(self._name)

    def include(self, child: BaseBlueprint) -> None:
        child.parent = self
        self._children.append(child)

    @abc.abstractmethod
    def run_setup(self): ...

    @abc.abstractmethod
    def run_startup(self, **kwargs): ...

    @abc.abstractmethod
    def run_shutdown(self): ...

    @abc.abstractmethod
    def run_destroy(self): ...

    @abc.abstractmethod
    def _notify(
        self,
        update: Update,
        event: TelegramType,
        type_: str,
        **kwargs
    ): ...
