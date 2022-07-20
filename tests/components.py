from dataclasses import dataclass, field

import cleangram as cg
from .conftest import TEST_TOKEN


@dataclass
class TestData:
    path: cg.TelegramPath
    result: cg.TelegramObject
    raw: dict = field(default_factory=dict)
    files: dict = field(default_factory=dict)

    def __str__(self):
        return self.path.__class__.__name__


PATH_RESULT_DATA = [
    TestData(
        cg.GetMe(),
        cg.User(id=int(TEST_TOKEN.split(":")[0]), first_name="Bot", is_bot=True)
    )
]
