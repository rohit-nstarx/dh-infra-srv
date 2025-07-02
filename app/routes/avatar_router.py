from fastapi import (
    APIRouter,
    Request,
    HTTPException,
    Depends,
)
from app.core.db.repository.avatar_repository import AvatarRepository
from app.core.logging import logger

avatar_router = APIRouter()
repo = AvatarRepository()


@avatar_router.get("/avatars")
def list_all_avatars():
    try:
        avatars = repo.fetch_all_avatars()
        return {"data": avatars}
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(status_code=500, detail="Unable to fetch avatars")


@avatar_router.get("/avatars/active")
def fetch_active_avatar():
    try:
        avatar = repo.fetch_active_avatar()
        if avatar:
            return {"data": avatar}
        raise Exception("Active avatar not found")
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(status_code=500, detail="Unable to fetch active avatar")


@avatar_router.post("/avatars/set-active-avatar/{id}")
def set_active_avatar(id: int):
    try:
        if repo.set_active_avatar(id):
            return {"message": "success"}
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(status_code=500, detail="Unable to set active avatar")


@avatar_router.get("/avatars/{id}")
def fetch_avatar_by_id(id: int):
    try:
        avatar = repo.fetch_avatar_by_id(id)
        return {"data": avatar}
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(status_code=500, detail="Unable to fetch avatar")
