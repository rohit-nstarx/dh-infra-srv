from app.core.llms import OllamaLLM

llm_map = {
    "ollama": OllamaLLM,
}

def get_llm(name: str):
    cls = llm_map.get(name)
    if not cls:
        raise ValueError(f"Unsupported LLM: {name}")
    return cls()
