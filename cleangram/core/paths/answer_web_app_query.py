from ...core.objects.response import Response
from ..objects import InlineQueryResult, SentWebAppMessage
from .base import TelegramPath


class AnswerWebAppQuery(TelegramPath, response=Response[SentWebAppMessage]):
    """
    Use this method to set the result of an interaction with a Web App and
    send a corresponding message on behalf of the user to the chat from
    which the query originated. On success, a SentWebAppMessage object is
    returned.

    Reference: https://core.telegram.org/bots/api#answerwebappquery
    """

    web_app_query_id: str
    """Unique identifier for the query to be answered"""

    result: InlineQueryResult
    """A JSON-serialized object describing the message to be sent"""
