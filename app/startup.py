import os
import time
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.orm import Session

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import RealDictCursor
import psycopg2

from .database import engine, Base
from .seed import seed_data
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

def ask_user_for_db_reset() -> bool:
    #respuesta = input("Do you want to delete and create the tables from scratch? (Y/n): ").strip().lower()
    respuesta = "yes"
    return respuesta in ["y", "yes", ""]

def create_database_if_not_exists():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        cursor.execute("SELECT 1 FROM pg_database WHERE datname=%s", (DB_NAME,))
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(f'CREATE DATABASE "{DB_NAME}"')
            print(f"Database '{DB_NAME}' created.")
        else:
            print(f"Database '{DB_NAME}' already exists.")

        cursor.close()
        conn.close()
    except Exception as e:
        print("Error creating database:", e)

def test_database_connection():
    while True:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                cursor_factory=RealDictCursor
            )
            print("Database connection successful")
            conn.close()
            break
        except Exception as error:
            print("Database connection failed")
            print("Error:", error)
            time.sleep(2)

@asynccontextmanager
async def lifespan(app: FastAPI):
    if os.getenv("ENV") == "local":
        if ask_user_for_db_reset():
            Base.metadata.drop_all(bind=engine)
            Base.metadata.create_all(bind=engine)
            db = Session(bind=engine)
            seed_data(db)
            db.close()
        else:
            print("Skipping table reset.")
    else:
        Base.metadata.create_all(bind=engine)

    yield
