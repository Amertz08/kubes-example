# TODO: write fake user repo and dep inject into tests


def test_create_user(client):
    input_data = {"username": "steve", "email": "steve@example.com"}
    response = client.post("/users", json=input_data)

    assert response.status_code == 201
    assert response.json() == {"id": 1, **input_data}
