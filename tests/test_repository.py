import repositories


def test_repository(setup_db, db_url):
    repo = repositories.UserRepository(db_url)

    username = "steve"
    email = "steve@example.com"

    result = repo.add(username, email)

    # TODO: accessing causes error
    assert result.username == username
    assert result.email == email
