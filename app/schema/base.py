from pydantic import BaseModel
from typing import Optional, List, Any


class SearchParameter(BaseModel):
    query: str
    collection_name: str
    limit: Optional[int] = 3
    query_embedding: List[List[Any]]


class DocumentResult(BaseModel):
    text: str
    chunk_id: int
    filename: str


class SearchResponse(BaseModel):
    results: List[DocumentResult]


class LLMQueryRequest(BaseModel):
    prompt: str



class LLMQueryData(BaseModel):
    model: str
    response: str
    created_at: str 

class LLMQueryResponse(BaseModel):
    response: LLMQueryData


class EmbedRequest(BaseModel):
    texts: list[str]


class ConversationCreate(BaseModel):
    user_query: str
    llm_response: str
