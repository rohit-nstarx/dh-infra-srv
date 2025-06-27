from fastapi import (
    APIRouter,
    Request,
    HTTPException,
    Depends,
    BackgroundTasks,
    UploadFile,
    File,
)
from fastapi.responses import JSONResponse

from app.config import env_var
from app.core.logging import logger
from app.core.llms import BaseLLM
from app.core.embeddings import BaseEmbedding
from app.core.vector_store import BaseVectorStore
from app.schema.base import SearchParameter, SearchResponse, DocumentResult, LLMQueryRequest, EmbedRequest
from app.core.mappings.llm_mappings import llm_map
from app.core.mappings.embeddings_mapping import embedding_map
from app.core.mappings.vector_strore_mappings import vector_store_map


router = APIRouter(tags=["RAG"])


@router.post("/llm/query")
def query_llm(query_request: LLMQueryRequest):
    try:
        llm: BaseLLM = llm_map[env_var.ACTIVE_LLM]
        return llm.query(prompt=query_request.prompt)
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(status_code=500, detail="Unable to query LLM")


@router.post("/embeddings/embed")
def generate_embedding(embedding_request: EmbedRequest):
    try:
        embedding: BaseEmbedding = embedding_map[env_var.ACTIVE_EMBEDDING]
        return embedding.embed(texts=embedding_request.texts)
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(status_code=500, detail="Unable to generate embedding")


@router.post("/vector/search")
def search_vector_store(param: SearchParameter) -> SearchResponse:
    try:
        vector_store: BaseVectorStore = vector_store_map[env_var.ACTIVE_VECTOR_STORE]
        raw_response = vector_store.search_documents(param.query, param.collection_name, param.limit)
        documents = raw_response["data"]["Get"]["Shi_hpe"]

        parsed = [DocumentResult(**{
            "text": doc["text"],
            "chunk_id": doc["chunk_id"],
            "filename": doc["filename"]
        }) for doc in documents]
        response = SearchResponse(results=parsed)

        return response
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(
            status_code=500, detail="Unable to perform similarity search"
        )
