from pydantic import BaseModel


class NewsletterResponse(BaseModel):
    dong_code: str
    title: str
    briefing: str
    weather: str
