import httpx
from app.core.logging import logger
from app.config import env_var
from app.core.utils.http_client import AsyncHttpClient

class ReadinessMixin:
    async def is_ready(self) -> bool:
        try:
            async with AsyncHttpClient() as client:
                response = await client.get(self.health_check_url)
                return response.status_code == 200
        except Exception as ex:
            logger.debug("Healthcheck Endpoint : ", self.health_check_url)
            logger.error(f"{self.__class__.__name__} health check failed: {ex}")
            return False