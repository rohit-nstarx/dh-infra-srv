from app.core.vector_store import WeaviateVectorStore

vector_store_map = {"weaviate": WeaviateVectorStore}

def get_vector_store(name: str):
    cls = vector_store_map.get(name)
    if not cls:
        raise ValueError(f"Unsupported vector store: {name}")
    return cls()

