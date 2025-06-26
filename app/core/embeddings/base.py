from abc import ABC, abstractmethod
from typing import List


class BaseEmbedding(ABC):
    @abstractmethod
    def embed(self, texts: List[str]) -> List[List[float]]:
        """Convert list of texts into list of embeddings"""
        pass
