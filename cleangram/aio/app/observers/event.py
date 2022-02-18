import asyncio


class EventObserver:
    def __init__(self):
        self.__events = []

    def register(self, event):
        self.__events.append(event)

    def __call__(self, event):
        self.register(event)
        return event

    def unregister(self, event):
        self.__events.remove(event)

    async def notify(self):
        await asyncio.gather(*[e() for e in self.__events])
