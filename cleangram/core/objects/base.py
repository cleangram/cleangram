from __future__ import annotations
from typing import TYPE_CHECKING

import pydantic


if TYPE_CHECKING:
    from ..bot.bot import Bot


class Component(pydantic.BaseModel):
    class Config:
        underscore_attrs_are_private = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class TelegramObject(Component):
    _bot: Bot

    def adjust(self, bot: Bot):
        self._bot = bot
