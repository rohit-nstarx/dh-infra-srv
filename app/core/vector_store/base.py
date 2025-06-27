from abc import ABC, abstractmethod
from typing import List, Any


class BaseVectorStore(ABC):
    @abstractmethod
    def add_documents(self, documents: List[dict], collection_name: str) -> None:
        """Add documents to the vector store"""
        pass

    @abstractmethod
    def search_documents(
        self, query_embedding: List[float], collection_name: str, limit: int = 3
    ):
        """Search for similar vectors and return top results"""
        pass

    @abstractmethod
    def is_ready(self) -> bool:
        """Return True if vector store is healthy"""
        pass
