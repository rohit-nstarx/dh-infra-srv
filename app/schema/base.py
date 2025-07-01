from pydantic import BaseModel
from typing import Optional, List


class SearchParameter(BaseModel):
    query: str
    collection_name: str
    limit: Optional[int] = 3


class DocumentResult(BaseModel):
    text: str
    chunk_id: int
    filename: str


class SearchResponse(BaseModel):
    results: List[DocumentResult]


class LLMQueryRequest(BaseModel):
    prompt: str


class LLMQueryResponse(BaseModel):
    model: str
    response: str
    created_at: str  # or datetime if you're parsing it


class EmbedRequest(BaseModel):
    texts: list[str]

class ConversationCreate(BaseModel):
    user_query: str
    llm_response: str