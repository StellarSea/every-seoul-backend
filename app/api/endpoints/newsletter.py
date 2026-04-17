from fastapi import APIRouter

from app.schemas.newsletter import NewsletterResponse

router = APIRouter()


@router.get("/", response_model=NewsletterResponse)
async def get_newsletter():
    return {"dong_code": "TODO", "title": "TODO", "briefing": "TODO", "weather": "TODO"}
