from abc import ABC, abstractmethod
from app.core.utils.common import ReadinessMixin
from typing import List


class BaseVectorStore(ReadinessMixin, ABC):
    @abstractmethod
    def search_documents(
        self, query_embedding: List[float], collection_name: str, limit: int = 3
    ):
        """Search for similar vectors and return top results"""
        pass
