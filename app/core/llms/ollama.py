import ollama
from app.core.llms.base import BaseLLM
from app.config import env_var


class OllamaLLM(BaseLLM):
    def __init__(self):
        super().__init__()
        self.client = ollama.Client(host=env_var.OLLAMA_BASE_URL)
