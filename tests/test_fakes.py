import schemas
from tests import fakes


class TestUserRepo:
    def test_add_will_add_user(self):
        repo = fakes.FakeUserRepo()

        username = "hello"
        email = "hello@example.com"

        result = repo.add(username, email)

        assert result == schemas.User(id=1, username=username, email=email)
