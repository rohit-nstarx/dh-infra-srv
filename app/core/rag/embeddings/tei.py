import httpx
from typing import List
from app.core.rag.embeddings.base import BaseEmbedding
from app.config import env_var
from app.core.logging import logger
from tenacity import retry, stop_after_attempt, wait_fixed


class TEIEmbedding(BaseEmbedding):
    def __init__(self):
        self.endpoint = f"{env_var.TEI_BASE_URL}:{env_var.TEI_PORT}"
        self.health_check_url = f"{self.endpoint}/health"

    @retry(stop=stop_after_attempt(env_var.RETRY_MAX_ATTEMPTS), wait=wait_fixed(env_var.RETRY_WAIT_SECONDS))
    def embed(self, texts: List[str]) -> List[List[float]]:
        response = httpx.post(self.endpoint, json={"inputs": texts}, timeout=10)
        logger.debug("status_code: %s", response.status_code)
        logger.debug("response_text: %s", response.text)

        if response.status_code != 200:
            raise Exception(f"TEI embedding service failed: {response.text}")
        return response.json()
