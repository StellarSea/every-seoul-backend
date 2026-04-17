from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(title="에브리 서울 API", version="1.0")

app.include_router(api_router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "에브리 서울 API"}
