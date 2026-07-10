from fastapi import FastAPI
import os

SERVER_ID = os.getenv("SERVER_ID", "X")

app = FastAPI()


@app.get("/")
async def root():
    return {"server": SERVER_ID}


@app.get("/health")
async def health():
    return {"status": "healthy"}
