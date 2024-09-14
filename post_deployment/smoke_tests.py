import httpx
import pytest

pytestmark = pytest.mark.smoke


@pytest.fixture()
def client():
    with httpx.Client(base_url="http://localhost:8000") as client:
        yield client


def test_root(client):
    response = client.get("/")

    assert response.status_code == 200


def test_health_check(client):
    response = client.get("/healthcheck")

    assert response.status_code == 200


def test_get_user_does_not_exist_returns_404(client):
    response = client.get("/user/does-not-exist")

    assert response.status_code == 404
