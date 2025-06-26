import httpx
from abc import ABC, abstractmethod

# services
from app.core.logging import logger


class Monitor:
    def __init__(self, url):
        self.url = url

    @property
    @abstractmethod
    def name(self):
        pass

    async def is_healthy(self):
        async with httpx.AsyncClient(timeout=2.0) as client:
            response = await client.get(self.url)
            return response.status_code == 200


class OllamaMonitor(Monitor):
    @property
    def name(self):
        return "ollama_service"

    async def is_healthy(self):
        try:
            return await super().is_healthy()
        except Exception as ex:
            logger.warning(f"Ollama health check failed: {ex}")
            return False


class WeaviateMonitor(Monitor):
    @property
    def name(self):
        return "weaviate_service"

    async def is_healthy(self):
        try:
            return await super().is_healthy()
        except Exception as ex:
            logger.warning(f"Weaviate health check failed: {ex}")
            return False
