import abc


class BaseObserver:
    @abc.abstractmethod
    def __call__(self, *args, **kwargs):
        ...

    @abc.abstractmethod
    def attach(self, listener, *args, **kwargs):
        ...

    @abc.abstractmethod
    def notify(self, *args, **kwargs):
        ...
