import pytest

import repositories

pytestmark = pytest.mark.integration


def test_can_add_user(setup_db, db_url):
    repo = repositories.UserRepository(db_url)

    username = "steve"
    email = "steve@example.com"

    result = repo.add(username, email)

    # TODO: accessing causes error AttributeError: 'NoneType' object has no attribute 'supports_population'
    assert result.username == username
    assert result.email == email


def test_can_get_user_if_exists(setup_db, db_url):
    repo = repositories.UserRepository(db_url)

    username = "steve"
    email = "steve@example.com"

    result = repo.add(username, email)
    user_id = result.id

    # TODO: accessing causes error AttributeError: 'NoneType' object has no attribute 'supports_population'
    result = repo.get(user_id)
    assert result.username == username


def test_get_no_user_found_returns_None(setup_db, db_url):
    result = repositories.UserRepository(db_url).get(123)
    assert result is None
