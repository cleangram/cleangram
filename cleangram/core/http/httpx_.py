import abc
from .base import Http


class BaseHttpX(Http, abc.ABC):
    @staticmethod
    def check(http_resp, path):
        return path.__response__.parse_raw(http_resp.content)
