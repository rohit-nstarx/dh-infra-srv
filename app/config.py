import os
from app.core.logging import logger

class EnvironmentVariables:
    # DH Services
    DH_ADMIN: str = os.getenv("DH_ADMIN", "103.160.145.247")
    DH_ADMIN_PORT: int = int(os.getenv("DH_ADMIN_PORT", "8000"))
    DH_ADMIN_HEALTH_ENDPOINT: str = "http://103.160.145.247:8000"

    DH_RAG_QUERY: str = os.getenv("DH_ADMIN", "103.160.145.247")
    DH_RAG_QUERY_PORT: int = int(os.getenv("DH_RAG_QUERY_PORT", "8000"))
    DH_RAG_QUERY_HEALTH_ENDPOINT: str = "http://103.160.145.247:8000"

    DH_AVATAR: str = os.getenv("DH_ADMIN", "103.160.145.247")
    DH_AVATAR_PORT: int = int(os.getenv("DH_AVATAR_PORT", "8000"))
    DH_AVATAR_HEALTH_ENDPOINT: str = "http://103.160.145.247:8000"

    # LLMs
    OLLAMA_HOST: str = os.getenv("OLLAMA_HOST", "http://localhost")
    OLLAMA_PORT: str = os.getenv("OLLAMA_PORT", "9001")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "tinyllama")
    OLLAMA_HEALTH_ENDPOINT: str = "http://localhost:9001/api/tags"

    # Embeddings
    TEI_BASE_URL: str = os.getenv("TEI_BASE_URL", "http://localhost")
    TEI_PORT: str = os.getenv("TEI_PORT", "9002")
    TEI_HEALTH_ENDPOINT: str = "http://localhost:9002/health"

    # Vector Store
    WEAVIATE_HOST: str = os.getenv("WEAVIATE_HOST", "http://localhost")
    WEAVIATE_PORT: int = int(os.getenv("WEAVIATE_PORT", "9003"))
    WEAVIATE_HEALTH_ENDPOINT: str = "http://localhost:9003/v1/.well-known/ready"

    # Logging and active configs
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "DEBUG")
    ACTIVE_LLM: str = os.getenv("ACTIVE_LLM", None)
    ACTIVE_EMBEDDING: str = os.getenv("ACTIVE_EMBEDDING", None)
    ACTIVE_VECTOR_STORE: str = os.getenv("ACTIVE_VECTOR_STORE", None)

    def __init__(self):
        self.monitored_services = {}
        for attr_name, value in vars(EnvironmentVariables).items():
            if attr_name.endswith("_HEALTH_ENDPOINT"):
                service_prefix = attr_name.removesuffix("_HEALTH_ENDPOINT")
                self.monitored_services[service_prefix] = value

# create instance
env_var = EnvironmentVariables()
