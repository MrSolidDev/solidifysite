import os

os.environ["SOLIDIFY_DATABASE_URL"] = "sqlite+pysqlite:///:memory:"
os.environ["SOLIDIFY_ADMIN_PASSWORD"] = "test-password"

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool
from pwdlib import PasswordHash

from app.database import Base, get_db
from app.main import app
from app.models import User

test_engine = create_engine("sqlite+pysqlite:///:memory:", connect_args={"check_same_thread": False}, poolclass=StaticPool)


def override_db():
    with Session(test_engine) as session:
        yield session


app.dependency_overrides[get_db] = override_db


@pytest.fixture(autouse=True)
def reset_database():
    Base.metadata.drop_all(test_engine)
    Base.metadata.create_all(test_engine)
    yield


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def admin_client(client):
    with Session(test_engine) as session:
        session.add(User(email="admin@test.local", password_hash=PasswordHash.recommended().hash("test-password")))
        session.commit()
    response = client.post("/api/auth/login", json={"email": "admin@test.local", "password": "test-password"})
    assert response.status_code == 200
    csrf = response.cookies["solidify_csrf"]
    return client, {"X-CSRF-Token": csrf}
