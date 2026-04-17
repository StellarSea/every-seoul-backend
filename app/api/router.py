from fastapi import APIRouter

from app.api.endpoints import newsletter

api_router = APIRouter()

api_router.include_router(newsletter.router, prefix="/newsletter", tags=["Newsletter"])
