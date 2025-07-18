from fastapi.testclient import TestClient
from app.main import app
from app import schemas

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.database import get_db
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from app.database import Base

import pytest

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}_test"
)

conn = psycopg2.connect(
        dbname="postgres",
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()
cursor.execute("SELECT 1 FROM pg_database WHERE datname=%s", (settings.DB_NAME + "_test",))
exists = cursor.fetchone()

if not exists:
    cursor.execute(f'CREATE DATABASE "{settings.DB_NAME}_test"')
    print(f"Database '{settings.DB_NAME}_test' created.")
else:
    print(f"Database '{settings.DB_NAME}_test' already exists.")

cursor.close()
conn.close()

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Fixtures
@pytest.fixture(scope="function")
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture(scope="function")
def test_user(client):
    user_data = {
        "email": "test@gmail.com",
        "password": "testpassword"
    }
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']  
    return new_user

