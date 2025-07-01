import httpx
import openai
from typing import List
from app.core.rag.embeddings.base import BaseEmbedding


class OpenAIEmbedding(BaseEmbedding):
    def __init__(self, model: str = "text-embedding-ada-002"):
        self.model = model

    def embed(self, texts: List[str]) -> List[List[float]]:
        response = openai.Embedding.create(model=self.model, input=texts)
        return [record["embedding"] for record in response["data"]]
