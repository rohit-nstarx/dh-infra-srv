from app.core.rag.llms import OllamaLLM
from app.config import env_var

llm_map = {
    "ollama": OllamaLLM,
}


def get_active_llm(name: str = env_var.ACTIVE_LLM):
    cls = llm_map.get(name)
    if not cls:
        raise ValueError(f"Unsupported LLM: {name}")
    return cls()
