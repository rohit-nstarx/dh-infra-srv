from app.core.embeddings import OpenAIEmbedding, TEIEmbedding

embedding_map = {
    "openai": OpenAIEmbedding,
    "tei": TEIEmbedding,
}

def get_embedding(name: str):
    cls = embedding_map.get(name)
    if not cls:
        raise ValueError(f"Unsupported embedding: {name}")
    return cls()
