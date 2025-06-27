import httpx
import asyncio

# services
from app.config import env_var
from app.core.logging import logger
from app.core.shared import ServiceStatusStore


class MonitoringService:
    def __init__(self):
        self.status = {}

    async def _check_service_status(self, service_name: str, endpoint: str) -> bool:
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                response = await client.get(endpoint, timeout=5)
                response.raise_for_status()
                return response.status_code == 200

        except Exception as e:
            logger.error(f"{service_name} healthcheck failed: %s", str(e))
            return False

    async def start_monitoring(self):
        i = 1
        while True:
            logger.info(f"Monitoring service: RUN {i}")
            service_names = env_var.monitored_services.keys()
            tasks = [
                self._check_service_status(service, endpoint)
                for service, endpoint in env_var.monitored_services.items()
            ]
            results = await asyncio.gather(*tasks)
            for service, result in zip(service_names, results):
                self.status[service] = result
                logger.info(f"{service}: {result}")
                await ServiceStatusStore.set_status(service_name=service, status=result)
            await asyncio.sleep(10)
            i = i + 1
