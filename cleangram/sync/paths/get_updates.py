from typing import List

from ...core.objects.response import Response
from ...core.paths.get_updates import GetUpdates as _GetUpdates
from ..objects import Update


class GetUpdates(_GetUpdates, response=Response[List[Update]]):
    """
    Use this method to receive incoming updates using long polling (wiki).
    An Array of Update objects is returned.

    Reference: https://core.telegram.org/bots/api#getupdates
    """
