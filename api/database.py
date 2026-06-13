import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id     SERIAL PRIMARY KEY,
            name   VARCHAR(100) NOT NULL,
            age    INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS cars (
            id     SERIAL PRIMARY KEY,
            name   VARCHAR(100) NOT NULL,
            model   VARCHAR(100) NOT NULL,
            yom    INTEGER NOT NULL
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()