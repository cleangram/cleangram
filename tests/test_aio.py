import contextlib
from unittest.mock import patch
import os

import httpx
import pytest
import respx

import cleangram as cg
from .components import PATH_RESULT_DATA, TestData

pytestmark = pytest.mark.asyncio

CUSTOM_URANDOM = os.urandom(16)


@respx.mock
@pytest.mark.parametrize(
    argnames="data",
    argvalues=PATH_RESULT_DATA,
    ids=lambda v: str(v))
@patch("os.urandom", lambda n: CUSTOM_URANDOM)
async def test_results(abot: cg.aio.Bot, data: TestData):
    url = abot.base_url(data.path)
    content = cg.Response(ok=True, result=data.result).json(exclude_none=True)

    with contextlib.ExitStack() as stack:
        files = {n: stack.enter_context(open(f.path, "rb")) for n, f in data.files.items()}
        request = httpx.Request(method="POST", url=url, data=data.raw, files=files)
        mock = respx.post(url, content=request.read()).mock(
            httpx.Response(200, content=content)
        )
        original_result = await abot(data.path)
        assert mock.called
        assert data.result == original_result
