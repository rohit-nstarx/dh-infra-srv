import httpx
from typing import List
from app.core.embeddings.base import BaseEmbedding

class TEIEmbedding(BaseEmbedding):
    def __init__(self, endpoint: str = "http://tei-svc:80/embed"):
        self.endpoint = endpoint

    def embed(self, texts: List[str]) -> List[List[float]]:
        response = httpx.post(self.endpoint, json={"inputs": texts}, timeout=10)

        if response.status_code != 200:
            raise Exception(f"TEI embedding service failed: {response.text}")

        return response.json()  # expected: list of vectors
