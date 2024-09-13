import pathlib

import pytest
import sqlalchemy

from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient

import main
import repositories
import tables

from tests import fakes


SRC_PATH = pathlib.Path(__file__).parent.parent.resolve() / "src"


@pytest.fixture()
def client() -> TestClient:
    a = main.app
    a.dependency_overrides[repositories.UserRepository] = fakes.FakeUserRepo()
    return TestClient(a)


@pytest.fixture(scope="session")
def db_url() -> str:
    return "sqlite:///test.db"


@pytest.fixture(scope="session")
def setup_db(db_url):
    cfg = Config(str(SRC_PATH / "alembic.ini"))

    eng = sqlalchemy.create_engine(db_url)
    tables.mapper_registry.metadata.create_all(eng)

    cfg.set_section_option("alembic", "sqlalchemy.url", db_url)
    cfg.set_section_option("alembic", "script_location", str(SRC_PATH / "migrations"))
    command.stamp(cfg, "head")
    tables.start_mappers()
    yield
    tables.mapper_registry.metadata.drop_all(eng)
