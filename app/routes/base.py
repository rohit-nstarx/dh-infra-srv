from fastapi import APIRouter, Request, HTTPException, Depends, BackgroundTasks, UploadFile, File
from fastapi.responses import JSONResponse

from app.config import env_var
from app.core.logging import logger
from app.core.llms.base import BaseLLM
from app.core.mappings import llm_map, embedding_map, vector_store_map
from app.core.embeddings.base import BaseEmbedding
from app.core.vector_store.base import BaseVectorStore


router = APIRouter(tags=["RAG"])


@router.post("/llm/query")
def query_llm(payload: dict):
    try:
        llm: BaseLLM = llm_map[env_var.ACTIVE_LLM]
        # return llm.query(payload)
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(status_code=500, detail="Unable to query LLM")


@router.post("/embeddings/generate")
def generate_embedding(payload: dict):
    try:
        embedding: BaseEmbedding = embedding_map[env_var.ACTIVE_EMBEDDING]
        # return embedding.embed(payload)
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(status_code=500, detail="Unable to generate embedding")


@router.post("/vector/search")
def search_vector_store(payload: dict):
    try:
        vector_store: BaseVectorStore = vector_store_map[env_var.ACTIVE_VECTOR_STORE]
        # return vector_store.similarity_search(payload)
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(status_code=500, detail="Unable to perform similarity search")
