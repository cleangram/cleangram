import json
from dataclasses import dataclass, field
from typing import Any

import cleangram as cg
from . import const


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
        cg.User(id=int(const.TEST_TOKEN.split(":")[0]), first_name="Bot", is_bot=True)
    ),

    TestData(
        cg.SetWebhook(
            url=const.TEST_URL,
            certificate=const.TEST_FILE
        ),
        True,
        {"url": const.TEST_URL},
        {"certificate": const.TEST_FILE}
    ),

    TestData(
        cg.GetWebhookInfo(),
        cg.WebhookInfo(
            url=const.TEST_URL,
            has_custom_certificate=False,
            pending_update_count=0,
        )
    ),

    TestData(
        cg.SendMessage(
            chat_id=const.TEST_CHAT_ID,
            text=const.TEST_TEXT
        ),
        cg.Message(
            message_id=const.TEST_MESSAGE_ID,
            date=const.TEST_MESSAGE_DATE,
            chat=cg.Chat(
                id=const.TEST_CHAT_ID,
                type=const.TEST_CHAT_TYPE
            ),
            text=const.TEST_TEXT
        ),
        dict(
            message_id=const.TEST_MESSAGE_ID,
            date=const.TEST_MESSAGE_DATE,
            chat=json.dumps(dict(
                id=const.TEST_CHAT_ID,
                type=const.TEST_CHAT_TYPE
            )),
            text=const.TEST_TEXT
        )
    )
]
