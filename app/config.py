import os
from app.core.logging import logger


import os
from typing import Optional


class EnvironmentVariables:
    # DH Services
    DH_ADMIN: Optional[str] = os.getenv("DH_ADMIN")
    DH_ADMIN_PORT: Optional[int] = int(os.getenv("DH_ADMIN_PORT")) if os.getenv("DH_ADMIN_PORT") else None
    DH_ADMIN_HEALTH_ENDPOINT: Optional[str] = os.getenv("DH_ADMIN_HEALTH_ENDPOINT")

    DH_RAG_QUERY: Optional[str] = os.getenv("DH_RAG_QUERY")
    DH_RAG_QUERY_PORT: Optional[int] = int(os.getenv("DH_RAG_QUERY_PORT")) if os.getenv("DH_RAG_QUERY_PORT") else None
    DH_RAG_QUERY_HEALTH_ENDPOINT: Optional[str] = os.getenv("DH_RAG_QUERY_HEALTH_ENDPOINT")

    DH_AVATAR: Optional[str] = os.getenv("DH_AVATAR")
    DH_AVATAR_PORT: Optional[int] = int(os.getenv("DH_AVATAR_PORT")) if os.getenv("DH_AVATAR_PORT") else None
    DH_AVATAR_HEALTH_ENDPOINT: Optional[str] = os.getenv("DH_AVATAR_HEALTH_ENDPOINT")

    # LLMs
    OLLAMA_HOST: Optional[str] = os.getenv("OLLAMA_HOST")
    OLLAMA_PORT: Optional[str] = os.getenv("OLLAMA_PORT")
    OLLAMA_MODEL: Optional[str] = os.getenv("OLLAMA_MODEL")
    OLLAMA_HEALTH_ENDPOINT: Optional[str] = os.getenv("OLLAMA_HEALTH_ENDPOINT")

    # Embeddings
    TEI_BASE_URL: Optional[str] = os.getenv("TEI_BASE_URL")
    TEI_PORT: Optional[str] = os.getenv("TEI_PORT")
    TEI_HEALTH_ENDPOINT: Optional[str] = os.getenv("TEI_HEALTH_ENDPOINT")

    # Vector Store
    WEAVIATE_HOST: Optional[str] = os.getenv("WEAVIATE_HOST")
    WEAVIATE_PORT: Optional[int] = int(os.getenv("WEAVIATE_PORT")) if os.getenv("WEAVIATE_PORT") else None
    WEAVIATE_HEALTH_ENDPOINT: Optional[str] = os.getenv("WEAVIATE_HEALTH_ENDPOINT")

    # Logging and config
    LOG_LEVEL: Optional[str] = os.getenv("LOG_LEVEL")
    HTTP_REQUEST_TIMEOUT: Optional[int] = int(os.getenv("HTTP_REQUEST_TIMEOUT")) if os.getenv("HTTP_REQUEST_TIMEOUT") else None
    SERVICE_HEALTH_CHECK_INTERVAL: Optional[int] = int(os.getenv("SERVICE_HEALTH_CHECK_INTERVAL")) if os.getenv("SERVICE_HEALTH_CHECK_INTERVAL") else None
    RETRY_WAIT_SECONDS: Optional[int] = int(os.getenv("RETRY_WAIT_SECONDS")) if os.getenv("RETRY_WAIT_SECONDS") else None
    RETRY_MAX_ATTEMPTS: Optional[int] = int(os.getenv("RETRY_MAX_ATTEMPTS")) if os.getenv("RETRY_MAX_ATTEMPTS") else None

    DB_HOST: Optional[str] = os.getenv("DB_HOST")
    DB_PORT: Optional[int] = int(os.getenv("DB_PORT")) if os.getenv("DB_PORT") else None
    DB_USER: Optional[str] = os.getenv("DB_USER")
    DB_NAME: Optional[str] = os.getenv("DB_NAME")
    DB_PASSWORD: Optional[str] = os.getenv("DB_PASSWORD")

    # Active components
    ACTIVE_LLM: Optional[str] = os.getenv("ACTIVE_LLM")
    ACTIVE_EMBEDDING: Optional[str] = os.getenv("ACTIVE_EMBEDDING")
    ACTIVE_VECTOR_STORE: Optional[str] = os.getenv("ACTIVE_VECTOR_STORE")

    def __init__(self):
        self.monitored_services = {}
        for attr_name, value in vars(EnvironmentVariables).items():
            if attr_name.endswith("_HEALTH_ENDPOINT"):
                service_prefix = attr_name.removesuffix("_HEALTH_ENDPOINT")
                self.monitored_services[service_prefix] = value


# create instance
env_var = EnvironmentVariables()
