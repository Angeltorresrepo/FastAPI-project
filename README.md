# FastAPI REST API

This project is a REST API built with FastAPI. It does not include a front-end interface; instead, it can be accessed via API clients such as Postman or through the automatically generated Swagger UI documentation available at /docs.

The application is containerized using Docker, allowing easy deployment and environment consistency. The Docker setup includes a separate PostgreSQL container for the database, and the API runs in its own container, managed via Docker Compose.

Using Docker and Docker Compose simplifies running the entire stack locally or in production, handling service dependencies and port mappings automatically.

---

## Functionalities:

- Basic endpoints for creating, reading, updating and deleting resources.
- Automatic Swagger UI documentation is available in the '/docs' directory.
- Simple validations and data handling with Pydantic.

---

## How to use:

1. Clone the repository.
2. Install the dependencies (e.g. using the command `pip install -r requirements.txt`).
3. Configure your PostgreSQL database connection by creating a `.env` file in the root folder with your database credentials (see next section).
4. Run the server with `uvicorn app.main:app --reload`.
5. Test the API from Postman or in the browser at [http://localhost:8000/docs](http://localhost:8000/docs).

---

## Database configuration

Before running the app, make sure you have PostgreSQL installed and running.

Create a `.env` file with the following variables, replacing the values with your own PostgreSQL credentials:

```env
DB_USER=your_postgres_username
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_NAME=your_database_name
ENV=local
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```
---
## Docker:

Specific commands to mount the app in docker (you must have docker desktop installed and running).

- **Basic usage**

- `docker build -t NAME .`
- `docker-compose -f FILE_NAME.yml (docker-compose-dev.yml) up -d`

- **Common Docker commands**

# Build the Docker image from the Dockerfile
`docker build -t image_name_desired .`

# Run container in foreground (useful for testing)
``docker run -p 8000:8000 image_name_desired``

# Run container in detached mode (background)
``docker run -d -p 8000:8000 image_name_desired``

# List Docker images
``docker images``

# List running containers
``docker ps``

# List all containers (including stopped)
``docker ps -a``

# View logs of a container (use container_id or name)
``docker logs <container_id>``

# Stop a running container
``docker stop <container_id>``

# Remove a container
``docker rm <container_id>``

# Remove an image
``docker rmi <image_id>``

# Start services defined in docker-compose.yml in detached mode
``docker-compose up -d``
``docker-compose -f FILE_NAME.yml up -d``

# Start services in interactive mode (not detached)
``docker-compose up``

# Stop and remove services and networks created by docker-compose
``docker-compose down``

# Rename the image
``docker image tag image_name_desired your_docker_name/your_repo_name``

# Push the image
``docker push your_docker_name/your_repo_name``

# Delete image
``docker rmi IMAGE_NAME:latest``
``docker rmi IMAGE-ID``


## Testing

This project includes automated tests covering authentication, posts management, and voting functionality.

- Tests use `pytest` and `TestClient` for simulating API requests.
- Fixtures setup test data like users, posts, and votes for consistent test environments.
- Includes tests for:
  - User login with correct and incorrect credentials
  - Access control: authorized vs unauthorized requests
  - CRUD operations on posts
  - Voting system including duplicate vote detection

