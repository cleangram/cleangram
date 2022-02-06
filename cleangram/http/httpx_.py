import httpx

from cleangram.http.base import Http


class HttpX(Http):
    def __init__(self):
        self.__client = httpx.AsyncClient()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self.__client.__aexit__(exc_type, exc_val, exc_tb)

    async def post(self, url: str, data: dict, files: dict, timeout: float) -> bytes:
        return (await self.__client.post(url, data=data, files=files, timeout=timeout)).content

    async def close(self):
        await self.__client.aclose()
