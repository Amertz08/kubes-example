# TODO: write fake user repo and dep inject into tests


def test_create_user(client):
    response = client.post("/users")

    assert response.status_code == 201
    assert response.json() == {"id": 1, "username": "hi", "email": "hello@example.com"}
