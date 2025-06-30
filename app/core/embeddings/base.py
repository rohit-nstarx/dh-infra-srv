import httpx
from typing import List
from abc import ABC, abstractmethod
from app.core.logging import logger
from app.core.utils.common import ReadinessMixin


class BaseEmbedding(ReadinessMixin, ABC):
    @abstractmethod
    def embed(self, texts: List[str]) -> List[List[float]]:
        """Convert list of texts into list of embeddings"""
        pass
