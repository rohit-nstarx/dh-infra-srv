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
from app.core.rag.llms import BaseLLM
from app.core.rag.embeddings import BaseEmbedding
from app.core.rag.vector_store import BaseVectorStore
from app.schema.base import (
    SearchParameter,
    SearchResponse,
    DocumentResult,
    LLMQueryRequest,
    EmbedRequest,
    LLMQueryResponse,
)
from app.core.rag.factory.llm_mappings import get_active_llm
from app.core.rag.factory.embeddings_mapping import get_active_embedding
from app.core.rag.factory.vector_strore_mappings import get_active_vector_store


router = APIRouter(tags=["RAG"])


@router.post("/llm/query")
def query_llm(query_request: LLMQueryRequest) -> LLMQueryResponse:
    try:
        llm: BaseLLM = get_active_llm()
        return llm.query(prompt=query_request.prompt)
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(status_code=500, detail="Unable to query LLM")


@router.post("/embedding/embed")
def generate_embedding(embedding_request: EmbedRequest):
    try:
        embedding: BaseEmbedding = get_active_embedding()
        return embedding.embed(texts=embedding_request.texts)
    except Exception as ex:
        logger.error(str(ex))
        raise HTTPException(status_code=500, detail="Unable to generate embedding")


@router.post("/vector/search")
async def search_vector_store(param: SearchParameter) -> SearchResponse:
    try:
        vector_store: BaseVectorStore = get_active_vector_store()
        documents = await vector_store.search_documents(
            param.query, param.collection_name, param.query_embedding, param.limit 
        )

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
