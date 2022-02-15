from .blueprint import Blueprint
from .workers import Polling
from ..utils import Presets


class App(Blueprint):
    def __init__(
        self,
        presets: Presets = None,
        **kwargs
    ) -> None:
        self.__presets = presets or Presets()
        super(App, self).__init__(**kwargs)

    @property
    def polling(self) -> Polling:
        return Polling(self, self.__presets)
