import cleangram as cg

import pytest_asyncio

from . import const


@pytest_asyncio.fixture
async def abot():
    async with cg.aio.Bot(const.TEST_TOKEN) as bot_:
        yield bot_


