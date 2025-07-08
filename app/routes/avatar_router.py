from fastapi import (
    APIRouter,
    Request,
    HTTPException,
    Depends,
)
from app.core.logging import logger

avatar_router = APIRouter()


@avatar_router.get("/avatars/active")
def fetch_active_avatar():
    try:
        return {"data": "kira"}
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(status_code=500, detail="Unable to fetch active avatar")


