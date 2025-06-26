import asyncio

# services
from app.core.logging import logger
from app.services.monitoring.base import Monitor, OllamaMonitor, WeaviateMonitor


class MonitoringService:
    def __init__(self):
        self.status = {}
        self.monitors = [
            OllamaMonitor(
                url="https://6656c1989f970b3b36c6624d.mockapi.io/api/v1/usrs"
            ),
            WeaviateMonitor(
                url="https://6656c1989f970b3b36c6624d.mockapi.io/api/v1/gg"
            ),
        ]

    async def start_monitoring(self):
        while True:
            logger.debug("monitoring server: running")
            tasks = [monitor.is_healthy() for monitor in self.monitors]
            results = await asyncio.gather(*tasks)
            for monitor, result in zip(self.monitors, results):
                self.status[monitor.name] = result
                logger.info(f"{monitor.name} is healthy: {result}")
            await asyncio.sleep(5)
