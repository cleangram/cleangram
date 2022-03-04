import json
from contextlib import ExitStack
from typing import Dict

from ...base.http.request import Request
from .base import AioHttp


class HttpX(AioHttp):
    def __init__(self):
        from httpx import AsyncClient

        self.__client = AsyncClient()

    async def __aenter__(self):
        await self.__client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.__client.__aexit__(exc_type, exc_val, exc_tb)

    async def close(self):
        await self.__client.aclose()

    async def json(self, request: Request) -> Dict:
        if request.files:
            data = {
                k: json.dumps(v) if isinstance(v, (dict, list)) else v
                for k, v in request.data.items()
            }
            with ExitStack() as stack:
                files = {n: stack.enter_context(f) for n, f in request.files.items()}
                response = await self.__client.post(
                    url=request.url, data=data, files=files, timeout=request.timeout
                )
        else:
            response = await self.__client.post(
                url=request.url, json=request.data, timeout=request.timeout
            )
        return response.json()
