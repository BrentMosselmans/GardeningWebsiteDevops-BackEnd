from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import test_connection
from queries.Brentqueries import create_tables, add_sample_data

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Testing database connection...")
    if not test_connection():
        print("Failed to connect to the database. Exiting...")
    else:
        print("Database connection successful!")
        create_tables()
        add_sample_data()
        print("Application is ready.")
    
    yield
    
    print("Application is shutting down.")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"message": "Hello World"}