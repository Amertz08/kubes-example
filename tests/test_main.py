import pytest

from fastapi.testclient import TestClient

import main


@pytest.fixture()
def client():
    return TestClient(main.app)


def test_root(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
