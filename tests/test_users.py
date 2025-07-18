from app import schemas
import pytest
from jose import jwt
from app.config import settings


#def test_root(client):
#    response = client.get("/")
#    assert response.status_code == 200
#    assert response.json().get('message') == "Welcome to the FastAPI application!"


def test_create_user(client):
    res = client.post("/users/", json = {
        "email": "hello123@gmail.com",
        "password": "password123"
    })

    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201

def test_login_user(client, test_user):
    
    res = client.post(
            "/login", data={
                "username": test_user['email'],
                "password": test_user['password']
            }
    )

    #Validate if the token is created correctly
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    id: str = payload.get("user_id")
    assert id == test_user['id']

    #Valid if the token type is correct
    assert login_res.token_type == "bearer"

    #Validate if the response is correct
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code",[
    ("wrongemail@gmail.com", "password123", 403),
    ("hello123@gmail.com", "wrongpassword", 403),
    ("wrongemail@gmail.com","wrongpassword", 403),
    ("","password123", 422),
    ("hello123@gmail.com", "", 422)

])
def test_incorrect_login(client,test_user, email, password, status_code):
    res = client.post("/login", data = {
        "username": email,
        "password":password
    })

    assert res.status_code == status_code
    