import httpx
from typing import List
from app.core.embeddings.base import BaseEmbedding
from app.config import env_var
from app.core.logging import logger

class TEIEmbedding(BaseEmbedding):
    def __init__(self):
        self.endpoint = f"{env_var.TEI_BASE_URL}:{env_var.TEI_PORT}"
        self.health_url = f"{self.endpoint}/health"  

    def embed(self, texts: List[str]) -> List[List[float]]:
        response = httpx.post(self.endpoint, json={"inputs": texts}, timeout=10)
        logger.debug("status_code: %s", response.status_code)
        logger.debug("response_text: %s", response.text)

        if response.status_code != 200:
            raise Exception(f"TEI embedding service failed: {response.text}")
        return response.json()

    def is_ready(self) -> bool:
        try:
            response = httpx.get(self.health_url, timeout=5)
            logger.debug("TEI health check response: %s", response.text)
            return response.status_code == 200
        except Exception as e:
            logger.error("TEI health check failed: %s", str(e))
            return False

    
