from dataclasses import dataclass, field
from typing import Any

import cleangram as cg
from .conftest import TEST_TOKEN


CERTIFICATE_FILE = cg.InputFile("README.md")


@dataclass
class TestData:
    path: cg.TelegramPath
    result: Any
    raw: dict = field(default_factory=dict)
    files: dict = field(default_factory=dict)

    def __str__(self):
        return self.path.__class__.__name__


PATH_RESULT_DATA = [
    TestData(
        cg.GetMe(),
        cg.User(id=int(TEST_TOKEN.split(":")[0]), first_name="Bot", is_bot=True)
    ),
    TestData(
        cg.SetWebhook(
            url="https://test.com",
            certificate=CERTIFICATE_FILE
        ),
        True,
        {"url": "https://test.com"},
        {"certificate": CERTIFICATE_FILE}
    )
]
