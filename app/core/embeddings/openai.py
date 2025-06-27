import httpx
import openai
from typing import List
from app.core.embeddings.base import BaseEmbedding


class OpenAIEmbedding(BaseEmbedding):
    def __init__(self, model: str = "text-embedding-ada-002"):
        self.model = model

    def embed(self, texts: List[str]) -> List[List[float]]:
        response = openai.Embedding.create(model=self.model, input=texts)
        return [record["embedding"] for record in response["data"]]

    async def is_ready(self) -> bool:
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                response = await client.get(self.health_check_url)
                response.raise_for_status()
                return response.status_code == 200
        except Exception as e:
            logger.error("Ollama health check failed: %s", str(e))
            return False
