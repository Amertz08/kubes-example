def test_root(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_healthcheck(client):
    response = client.get("/healthcheck")
    assert response.status_code == 200
