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
        parent: Optional[BaseBlueprint] = None,
        children: List[BaseBlueprint] = (),
        deps: Dict[str, Any] = None,
        flags: Dict[str, Any] = None,
        **kwargs
    ) -> None:
        self._name = name
        self._log = logging.getLogger(name)
        self._filters = filters
        self._parent = parent
        self._children = children
        self._deps = deps or {}
        self._flags = flags or {}
        self._handler_observers = {
            name: obs for name, obs in vars(self).items()
            if isinstance(obs, BaseHandlerObserver)
        }

    # @property
    # def children(self) -> List[BaseBlueprint]:
    #     return self._children
    #
    # @property
    # def deps(self) -> Dict[str, Any]:
    #     return self.__deps
    #
    # @property
    # def flags(self) -> Dict[str, Any]:
    #     return self.__flags
    #
    # @property
    # def handler_observers(self) -> Dict[str, BaseHandlerObserver]:
    #     return self.__handler_observers
    #

    @property
    def log(self):
        return self._log

    @property
    def deps(self):
        return self._deps

    @property
    def parent(self) -> BaseBlueprint:
        return self._parent

    @property
    def root(self) -> BaseBlueprint:
        _root = self
        while parent := _root.parent:
            _root = parent
        return _root

    @parent.setter
    def parent(self, _parent):
        self._parent = _parent

    def include(self, children: BaseBlueprint) -> None:
        children.parent = self
        self._children.append(children)

    @property
    def children(self):
        return self._children

    @abc.abstractmethod
    def run_setup(self): ...

    @abc.abstractmethod
    def run_startup(self, **kwargs): ...

    @abc.abstractmethod
    def run_shutdown(self): ...

    @abc.abstractmethod
    def run_destroy(self): ...

    @abc.abstractmethod
    def notify(self, update: Update, bot, **kwargs): ...

    @abc.abstractmethod
    def _notify_event(self, update: Update, event: TelegramType, type_: str, **kwargs): ...
