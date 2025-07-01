import json
import httpx
import weaviate
from weaviate.classes.query import MetadataQuery
from typing import List
from app.core.rag.vector_store.base import BaseVectorStore
from app.core.rag.embeddings.base import BaseEmbedding
from app.config import env_var
from app.core.logging import logger
from app.core.rag.factory.embeddings_mapping import get_active_embedding
from app.core.utils.http_client import AsyncHttpClient
from tenacity import retry, stop_after_attempt, wait_fixed

class WeaviateVectorStore(BaseVectorStore):
    def __init__(self):
        self.base_url = f"{env_var.WEAVIATE_HOST}:{env_var.WEAVIATE_PORT}"
        self.health_check_url = f"{self.base_url}/v1/.well-known/ready"

    def _get_embeddings(self, query):
            embedding: BaseEmbedding = get_active_embedding()
            return embedding.embed(query)[0]

    @retry(stop=stop_after_attempt(env_var.RETRY_MAX_ATTEMPTS), wait=wait_fixed(env_var.RETRY_WAIT_SECONDS))
    async def _query_vector_store(self, collection_name, query_embedding, limit):
        graphql_query = {
            "query": f"""
            {{
                Get {{
                    {collection_name}(
                        nearVector: {{
                            vector: {json.dumps(query_embedding)}
                        }}
                        limit: {limit}
                    ) {{
                        text
                        filename
                        chunk_id
                        _additional {{
                            distance
                        }}
                    }}
                }}
            }}
            """
        }

        async with AsyncHttpClient() as client:
            response = await client.post(
                f"{self.base_url}/v1/graphql",
                json=graphql_query,
                headers={"Content-Type": "application/json"},
            )

            print(f"GraphQL response status: {response.status_code}")
            result = response.json()
            return result
         

    async def search_documents(self, query: str, collection_name: str, limit: int = 3):
        try:
            query_embedding = self._get_embeddings(query=query)
            raw_response = await self._query_vector_store(collection_name=collection_name, query_embedding=query_embedding, limit=limit)
            documents = raw_response["data"]["Get"][collection_name]
            return documents
        except Exception as e:
            logger.error(f"Search failed: {e}")
            return []
