import httpx
import ollama
from typing import List
from app.core.llms.base import BaseLLM
from app.config import env_var
from app.core.logging import logger


class OllamaLLM(BaseLLM):
    def __init__(self):
        super().__init__()
        self.base_url = f"{env_var.OLLAMA_HOST}:{env_var.OLLAMA_PORT}"
        self.health_check_url = f"{self.base_url}/api/tags"

    async def is_ready(self) -> bool:
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                response = await client.get(self.health_check_url)
                response.raise_for_status()
                return response.status_code == 200
        except Exception as e:            
            logger.error("Ollama health check failed: %s", str(e))            
            logger.debug(f"Ollama endpoint {self.health_check_url}")
            return False
        
    def query(self, prompt: str, **kwargs) -> str:
            try:
                response = httpx.post(
                    f"{self.base_url}/api/generate",
                    json={
                        "model": env_var.OLLAMA_MODEL,
                        "prompt": prompt,
                        "stream": False,  # Set to True if you want streaming
                        "options": {
                            "temperature": 0.6,    # Controls randomness (0.0 = deterministic, 1.0 = very random)
                            "top_p": 0.7,          # Nucleus sampling (0.1 = only top 10% likely tokens)
                            "num_predict": 1024    # Maximum tokens to generate
                        }
                    },
                    headers={"Content-Type": "application/json"},
                    timeout=60.0  # Adjust timeout as needed
                )
                
                if response.status_code == 200:
                    result = response.json()
                    print(result)
                    return result
                else:
                    return {
                        "error": f"HTTP {response.status_code}",
                        "details": response.text
                    }
                    
            except Exception as e:
                return {"error": f"Request failed: {e}"}
