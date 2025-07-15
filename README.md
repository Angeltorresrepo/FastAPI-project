The project consists of a REST API created with FastAPI. It has no front-end interface and is accessible via tools such as Postman, or via the automatic documentation at /docs.

## Functionalities:

- Basic endpoints for creating, reading, updating and deleting resources.
- Automatic Swagger UI documentation is available in the '/docs' directory.
- Simple validations and data handling with Pydantic.

## How to use:

1. Clone the repository.
2. Install the dependencies (e.g. using the command `pip install -r requirements.txt`).
3. Configure your PostgreSQL database connection by creating a `.env` file in the root folder with your database credentials (see next section).
4. Run the server with `uvicorn app.main:app --reload`.
5. Test the API from Postman or in the browser at [http://localhost:8000/docs](http://localhost:8000/docs).

## Database configuration

Before running the app, make sure you have PostgreSQL installed and running.

Create a `.env` file with the following variables, replacing the values with your own PostgreSQL credentials:

```env
DB_USER=your_postgres_username
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_NAME=your_database_name
