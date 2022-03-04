import pytest

from cleangram.base.client.api import Api


def test_api():
    api = Api()
    assert not api.local
    assert api.url == "https://api.telegram.org"

