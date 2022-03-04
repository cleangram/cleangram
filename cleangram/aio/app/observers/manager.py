import contextlib
import functools


class ContextManagerObserver:
    def __init__(self):
        self.__managers = []

    def attach(self, manager):
        self.__managers.append(contextlib.asynccontextmanager(manager))

    def __call__(self, manager):
        self.attach(manager)
        return manager

    @contextlib.asynccontextmanager
    async def notify(self, *args, **kwargs):
        async with contextlib.AsyncExitStack() as stack:
            output = {}
            for manager in self.__managers:
                manager = functools.partial(manager, *args, **kwargs, **output)
                if isinstance(processed := await stack.enter_async_context(manager()), dict):
                    output.update(processed)
            yield output
