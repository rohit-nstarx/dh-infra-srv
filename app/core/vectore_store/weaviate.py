import weaviate
from weaviate.classes.query import MetadataQuery
from typing import List
from app.core.vectore_store.base import BaseVectorStore

from app.config import env_var
from app.core.logging import logger


class WeaviateVectorStore(BaseVectorStore):
    def __init__(self):
        self.client = weaviate.connect_to_local(
            host=env_var.WEAVIATE_HOST,
            port=env_var.WEAVIATE_PORT,
        )

    def is_ready(self) -> bool:
        return self.client.is_ready()

    def search(self, query_embedding: List[float], collection_name: str, limit: int = 3):
        try:
            collection = self.client.collections.get(collection_name)
            results = collection.query.near_vector(
                near_vector=query_embedding,
                limit=limit,
                return_metadata=MetadataQuery(distance=True)
            )

            return [
                dict(
                    text=obj.properties["text"],
                    filename=obj.properties["filename"],
                    chunk_id=obj.properties["chunk_id"],
                    distance=obj.metadata.distance,
                )
                for obj in results.objects
            ]

        except Exception as e:
            logger.error(f"Search failed: {e}")
            return []
