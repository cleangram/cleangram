import cleangram as cg

import pytest_asyncio

TEST_TOKEN = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"


@pytest_asyncio.fixture
async def abot():
    async with cg.aio.Bot(TEST_TOKEN) as bot_:
        yield bot_


