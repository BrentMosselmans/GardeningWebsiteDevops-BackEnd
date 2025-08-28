from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import test_connection
from queries.Brentqueries import create_tables, add_sample_data
from Routes.BrentEndpoints import router as brent_router
from Models.Brentmodels import SeasonalTip
from fastapi.middleware.cors import CORSMiddleware

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

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"]
)

app.include_router(brent_router)

@app.get("/")
def root():
    return {"message": "Hello World"}
