from app.core.llms.ollama import OllamaLLM
from app.core.embeddings.openai import OpenAIEmbedding
from app.core.embeddings.tei import TEIEmbedding
from app.core.vector_store.weaviate import WeaviateVectorStore

llm_map = {
    "ollama": OllamaLLM,
}

embedding_map = {
    "openai": OpenAIEmbedding,
    "tei": TEIEmbedding
}


vector_store_map = {
    "weaviate": WeaviateVectorStore
}

