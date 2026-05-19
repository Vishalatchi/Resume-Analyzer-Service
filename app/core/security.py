from fastapi import Header, HTTPException
from app.core.settings import settings


async def validate_api_key(x_api_key: str = Header(...)):

    if x_api_key != settings.API_AUTH_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )