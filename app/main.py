from fastapi import FastAPI
from .routers import post, user, auth, votes

from .startup import create_database_if_not_exists, test_database_connection, lifespan

create_database_if_not_exists()
test_database_connection()

app = FastAPI(lifespan=lifespan)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI application!"}
