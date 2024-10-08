import pytest

import schemas
from tests import fakes

pytestmark = pytest.mark.unit


class TestUserRepo:
    def test_add_will_add_user(self):
        repo = fakes.FakeUserRepo()

        username = "hello"
        email = "hello@example.com"

        result = repo.add(username, email)

        assert result == schemas.User(id=1, username=username, email=email)

    def test_get_can_get_user(self):
        repo = fakes.FakeUserRepo()

        username = "hello"
        email = "hello@example.com"

        result = repo.add(username, email)

        observed = repo.get(result.id)

        assert observed == schemas.User(id=1, username=username, email=email)
