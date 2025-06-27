from fastapi import (
    APIRouter,
    Request,
    HTTPException,
    Depends,
    BackgroundTasks,
    UploadFile,
    File,
)
from app.core.logging import logger
from app.core.llms import BaseLLM
from app.core.embeddings import BaseEmbedding
from app.core.vector_store import BaseVectorStore
from app.schema.base import (
    SearchParameter,
    SearchResponse,
    DocumentResult,
    LLMQueryRequest,
    EmbedRequest,
)
from app.core.factory.llm_mappings import get_active_llm
from app.core.factory.embeddings_mapping import get_active_embedding
from app.core.factory.vector_strore_mappings import get_active_vector_store


router = APIRouter(tags=["RAG"])


@router.post("/llm/query")
def query_llm(query_request: LLMQueryRequest):
    try:
        llm: BaseLLM = get_active_llm()
        return llm.query(prompt=query_request.prompt)
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(status_code=500, detail="Unable to query LLM")


@router.post("/embeddings/embed")
def generate_embedding(embedding_request: EmbedRequest):
    try:
        embedding: BaseEmbedding = get_active_embedding()
        return embedding.embed(texts=embedding_request.texts)
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(status_code=500, detail="Unable to generate embedding")


@router.post("/vector/search")
def search_vector_store(param: SearchParameter) -> SearchResponse:
    try:
        vector_store: BaseVectorStore = get_active_vector_store()
        raw_response = vector_store.search_documents(
            param.query, param.collection_name, param.limit
        )
        documents = raw_response["data"]["Get"]["Shi_hpe"]

        parsed = [
            DocumentResult(
                **{
                    "text": doc["text"],
                    "chunk_id": doc["chunk_id"],
                    "filename": doc["filename"],
                }
            )
            for doc in documents
        ]
        response = SearchResponse(results=parsed)

        return response
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(
            status_code=500, detail="Unable to perform similarity search"
        )
