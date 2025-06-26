import os


class EnvironmentVariables:
    # LLms
    OLLAMA_BASE_URL: str = ""

    # Embeddings

    # Vector Store

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "DEBUG")

    ACTIVE_LLM: str = os.getenv("ACTIVE_LLM", None) # ollama, openai
    ACTIVE_EMBEDDING: str = os.getenv("ACTIVE_EMBEDDING", None)
    ACTIVE_VECTOR_STORE: str = os.getenv("ACTIVE_VECTOR_STORE", None)


# create instance
env_var = EnvironmentVariables()
