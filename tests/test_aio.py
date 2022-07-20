import httpx
import pytest
import respx

import cleangram as cg
from .components import PATH_RESULT_DATA

pytestmark = pytest.mark.asyncio


@respx.mock
@pytest.mark.parametrize(
    argnames="data",
    argvalues=PATH_RESULT_DATA,
    ids=lambda v: str(v))
async def test_results(abot: cg.aio.Bot, data):
    async with respx.mock:
        mock = respx.post(abot.base_url(data.path)).mock(
            httpx.Response(200, content=cg.Response(ok=True, result=data.result).json(exclude_none=True))
        )
        original_result = await abot(data.path)
        # original_result.id = 33
        assert mock.called
        assert data.result == original_result
