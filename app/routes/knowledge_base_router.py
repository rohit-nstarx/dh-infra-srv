from fastapi import (
    APIRouter,
    Request,
    HTTPException,
    Depends,
)
from app.core.db.repository.knowledge_base_repository import KnowledgeBaseRepository
from app.core.logging import logger

knowlege_router = APIRouter()


@knowlege_router.get("/knowledge-base")
def fetch_latest_knowledge_base():
    try:
        repo = KnowledgeBaseRepository()
        knowledge = repo.fetch_latest_knowledge_base()
        return {"data": knowledge}
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(status_code=500, detail="Unable to fetch data")
