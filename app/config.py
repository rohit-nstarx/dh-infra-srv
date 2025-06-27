import os


class EnvironmentVariables:
    # DH Services
    DH_ADMIN: str = os.getenv("DH_ADMIN", "103.160.145.247")
    DH_ADMIN_PORT: int = int(os.getenv("DH_ADMIN_PORT", "8000"))
    DH_ADMIN_HEALTH_ENDPOINT: str = "/"

    DH_RAG_QUERY: str = os.getenv("DH_ADMIN", "103.160.145.247")
    DH_RAG_QUERY_PORT: int = int(os.getenv("DH_RAG_QUERY_PORT", "8000"))
    DH_RAG_QUERY_HEALTH_ENDPOINT: str = "/"

    DH_AVATAR: str = os.getenv("DH_ADMIN", "103.160.145.247")
    DH_AVATAR_PORT: int = int(os.getenv("DH_AVATAR_PORT", "8000"))
    DH_AVATAR_HEALTH_ENDPOINT: str = "/"



    # LLms
    OLLAMA_HOST: str = os.getenv("OLLAMA_HOST", "localhost")
    OLLAMA_PORT: str = os.getenv("OLLAMA_PORT", "11435")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "tinyllama")
    # OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "tinyllama")

    # Embeddings
    TEI_BASE_URL: str = os.getenv("TEI_BASE_URL", "http://tei-svc")
    TEI_PORT: str = os.getenv("TEI_PORT", "80")

    # Vector Store
    WEAVIATE_HOST: str = os.getenv("WEAVIATE_HOST", "weaviate-svc")
    WEAVIATE_PORT: int = int(os.getenv("WEAVIATE_PORT", "8080"))

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "DEBUG")

    ACTIVE_LLM: str = os.getenv("ACTIVE_LLM", None)  # ollama, openai
    ACTIVE_EMBEDDING: str = os.getenv("ACTIVE_EMBEDDING", None)
    ACTIVE_VECTOR_STORE: str = os.getenv("ACTIVE_VECTOR_STORE", None)


# create instance
env_var = EnvironmentVariables()
