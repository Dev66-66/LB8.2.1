from fastapi import FastAPI
from .api.tips import get_router

app = FastAPI(title="Tip of the Day API")


app.include_router(get_router(), prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to Tip of the Day API"}