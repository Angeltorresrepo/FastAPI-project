from fastapi.testclient import TestClient
from app.main import app
from app import schemas, models

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.database import get_db
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from app.database import Base

import pytest

from app.oauth2 import create_access_token

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

@pytest.fixture(scope="function")
def test_user2(client):
    user_data = {
        "email": "test2@gmail.com",
        "password": "testpassword"
    }
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']  
    return new_user

@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})


@pytest.fixture
def authorized_client(client,token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client

@pytest.fixture
def test_posts(test_user, session, test_user2):
    posts_data = [
        {
            "title": "1st title",
            "content": "1st content",
            "owner_id":test_user['id']
        },
        {
            "title": "2nd title",
            "content": "2nd content",
            "owner_id":test_user['id']
        },
        {
            "title": "3rd title",
            "content": "3rd content",
            "owner_id":test_user['id']
        },
        {
            "title": "3rd title",
            "content": "3rd content",
            "owner_id":test_user2['id']
        }
    ]

    def create_post_model(post):
        return models.Post(**post)

    post_map = map(create_post_model, posts_data)
    posts = list(post_map)

    session.add_all(posts)


    #session.add_all([
    #    models.User(title = "", content = "", owner_id=test_user["id"]),
    #    models.User(title = "", content = "", owner_id=test_user["id"]),
    #    models.User(title = "", content = "", owner_id=test_user["id"]) 
    #    ])

    session.commit()
    posts = session.query(models.Post).all()
    return posts


@pytest.fixture()
def test_vote(test_posts, session, test_user):
    new_vote = models.Vote(post_id=test_posts[3].id, user_id=test_user['id'])
    session.add(new_vote)
    session.commit()

