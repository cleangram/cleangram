from time import time

import cleangram as cg


TEST_TOKEN = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
TEST_BOT_ID = int(TEST_TOKEN.split(":")[0])
TEST_FILE = cg.InputFile("README.md")
TEST_URL = "https://test.com"
TEST_CHAT_ID = 34144734
TEST_CHAT_TYPE = "private"
TEST_TEXT = "Hello User"
TEST_MESSAGE_ID = 2
TEST_MESSAGE_DATE = int(time())
