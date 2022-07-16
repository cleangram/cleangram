import abc

from .http import Http


class BaseHttp(Http, abc.ABC):
    ...
