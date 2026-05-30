from time import sleep

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/api/health")
async def health():
    db_info = settings.DATABASE_URL.split("@")[1]
    return {"message": db_info}

@app.get("/api/hello")
async def root():
    sleep(5)
    return {"message": "Hello World!!!"}