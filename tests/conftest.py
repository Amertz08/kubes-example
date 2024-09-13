import pytest

from fastapi.testclient import TestClient

import main
import repositories

from tests import fakes


@pytest.fixture()
def client() -> TestClient:
    a = main.app
    a.dependency_overrides[repositories.UserRepository] = fakes.FakeUserRepo()
    return TestClient(a)
