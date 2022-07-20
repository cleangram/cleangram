from dataclasses import dataclass, field
from typing import Any

import cleangram as cg
from .conftest import TEST_TOKEN


TEST_FILE = cg.InputFile("README.md")
TEST_URL = "https://test.com"


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
            url=TEST_URL,
            certificate=TEST_FILE
        ),
        True,
        {"url": TEST_URL},
        {"certificate": TEST_FILE}
    ),
    TestData(
        cg.GetWebhookInfo(),
        cg.WebhookInfo(
            url=TEST_URL,
            has_custom_certificate=False,
            pending_update_count=0,
        )
    )
]
