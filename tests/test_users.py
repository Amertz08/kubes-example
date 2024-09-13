def test_create_user(client):
    input_data = {"username": "steve", "email": "steve@example.com"}
    response = client.post("/users", json=input_data)

    assert response.status_code == 201
    assert response.json() == {"id": 1, **input_data}


def test_can_get_user(client):
    input_data = {"username": "steve", "email": "steve@example.com"}
    response = client.post("/users", json=input_data)

    assert response.status_code == 201

    user_data = response.json()

    response = client.get(f"/users/{user_data['id']}")
    assert response.status_code == 200
    assert response.json() == user_data
