import asyncio

from .base import Observer


class EventsObserver(Observer):
    def __init__(self):
        self._events = []

    def register(self, event):
        if event not in self._events:
            self._events.append(event)

    def __call__(self, event):
        self.register(event)

    def unregister(self, event):
        self._events.remove(event)

    async def notify(self):
        await asyncio.gather(*[e() for e in self._events])
