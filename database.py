import os
import psycopg
from dotenv import load_dotenv

# Load env. file
load_dotenv()

# Get databse url from env
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to the database
def get_connection():
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL environment variable is not set.")
    return psycopg.connect(conninfo=DATABASE_URL)

# test database connection
def test_connection():
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
        print("Database connection successful!")
        conn.close()
        return True
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False