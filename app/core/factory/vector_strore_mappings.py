from app.core.vector_store import WeaviateVectorStore
from app.config import env_var

vector_store_map = {"weaviate": WeaviateVectorStore}


def get_active_vector_store(name: str = env_var.ACTIVE_VECTOR_STORE):
    cls = vector_store_map.get(name)
    if not cls:
        raise ValueError(f"Unsupported vector store: {name}")
    return cls()
