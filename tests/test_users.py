def test_create_user(client):
    response = client.post("/users")

    assert response.status_code == 201
    assert response.json() == {}
