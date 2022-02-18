from contextlib import ExitStack

import json

from typing import Dict

from .base import SyncHttp
from ...base.http.request import Request


class HttpX(SyncHttp):
    def __init__(self):
        from httpx import Client

        self.__client = Client()

    def __enter__(self):
        self.__client.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__client.__exit__(exc_type, exc_val, exc_tb)

    def close(self):
        self.__client.close()

    def json(self, request: Request) -> Dict:
        if request.files:
            data = {
                k: json.dumps(v) if isinstance(v, (dict, list)) else v
                for k, v in request.data.items()
            }
            with ExitStack() as stack:
                files = {n: stack.enter_context(f) for n, f in request.files.items()}
                response = self.__client.post(
                    url=request.url, data=data, files=files, timeout=request.timeout
                )
        else:
            response = self.__client.post(
                url=request.url, json=request.data, timeout=request.timeout
            )
        return response.json()
