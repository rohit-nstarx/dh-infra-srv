import json
import httpx
import weaviate
from weaviate.classes.query import MetadataQuery
from typing import List
from app.core.vector_store.base import BaseVectorStore
from app.core.embeddings.base import BaseEmbedding
from app.config import env_var
from app.core.logging import logger
from app.core.factory.embeddings_mapping import get_active_embedding


class WeaviateVectorStore(BaseVectorStore):
    def __init__(self):
        self.base_url = f"{env_var.WEAVIATE_HOST}:{env_var.WEAVIATE_PORT}"
        self.health_check_url = f"{self.base_url}/v1/.well-known/ready"
    
    async def is_ready(self) -> bool:
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                response = await client.get(self.health_check_url)
                response.raise_for_status()
                return response.status_code == 200
        except Exception as e:
            logger.error(f"Weaviate readiness check failed: {e}")
            logger.debug("Weviate healh check url: %s", self.health_check_url)
            return False

    def search_documents(
        self, query: str, collection_name: str, limit: int = 3
    ):
        try:
            embedding: BaseEmbedding = get_active_embedding()           
            query_embedding = embedding.embed(query)[0] # httpx.post(, json={"inputs": [query]}).json()[0]

            print('embeddings done')
            # Prepare GraphQL query for vector search
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
            
            # Make HTTP request to GraphQL endpoint
            response = httpx.post(
                f"{self.base_url}/v1/graphql",
                json=graphql_query,
                headers={"Content-Type": "application/json"}
            )
            
            print(f"GraphQL response status: {response.status_code}")
            result = response.json()
            return result

        except Exception as e:
            logger.error(f"Search failed: {e}")
            return []
