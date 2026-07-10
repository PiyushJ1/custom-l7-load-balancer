from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"server": 1}

@app.get("/health")
async def health():
    return {"status": "healthy"}
