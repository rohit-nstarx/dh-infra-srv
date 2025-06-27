import json
import httpx
import weaviate
from weaviate.classes.query import MetadataQuery
from typing import List
from app.core.vector_store.base import BaseVectorStore
from app.core.embeddings.base import BaseEmbedding
from app.config import env_var
from app.core.logging import logger
from app.core.factory.embeddings_mapping import get_embedding


class WeaviateVectorStore(BaseVectorStore):
    def __init__(self):
        print(env_var.WEAVIATE_HOST)
        print(env_var.WEAVIATE_PORT)
        self.base_url = f"http://{env_var.WEAVIATE_HOST}:{env_var.WEAVIATE_PORT}"
        self.client = weaviate.connect_to_local(
            host=env_var.WEAVIATE_HOST,
            port=int(env_var.WEAVIATE_PORT),
            skip_init_checks=True
        )

    def is_ready(self) -> bool:
        try:
            ready = self.client.is_ready()
            logger.debug(f"Weaviate readiness: {ready}")
            return ready
        except Exception as e:
            logger.error(f"Weaviate readiness check failed: {e}")
            return False

    def add_documents(self, documents: List[dict], collection_name: str) -> None:
        """Add documents to the vector store"""
        pass

    def search_documents(
        self, query: str, collection_name: str, limit: int = 3
    ):
        try:
            embedding: BaseEmbedding = get_embedding(env_var.ACTIVE_EMBEDDING)           
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
