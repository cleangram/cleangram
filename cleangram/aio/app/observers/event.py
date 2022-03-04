import abc

import asyncio
import functools
from typing import TYPE_CHECKING

from cleangram.base.app.blueprint import BaseBlueprint
from cleangram.base.app.observers import BaseEventObserver


class EventObserver(BaseEventObserver):
    def __init__(self, blueprint: BaseBlueprint):
        self.__blueprint = blueprint
        self.__events = []

    def attach(self, event):
        self.__events.append(event)

    def __call__(self, event):
        self.attach(event)
        return event

    async def notify(self, **kwargs):
        e_kwargs = {}
        for event in self.__events:
            if kw := await functools.partial(event)():
                e_kwargs.update(kw)
        return e_kwargs
