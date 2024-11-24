from fastapi import FastAPI
from .routes import router as items_router

app = FastAPI()

app.include_router(items_router, prefix="/api", tags=["items"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
