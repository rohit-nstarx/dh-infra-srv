from app.core.embeddings import OpenAIEmbedding, TEIEmbedding
from app.config import env_var

embedding_map = {
    "openai": OpenAIEmbedding,
    "tei": TEIEmbedding,
}


def get_active_embedding(name: str = env_var.ACTIVE_EMBEDDING):
    cls = embedding_map.get(name)
    if not cls:
        raise ValueError(f"Unsupported embedding: {name}")
    return cls()
