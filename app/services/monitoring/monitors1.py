import httpx
from abc import ABC, abstractmethod

# services
from app.core.logging import logger


class Monitor(ABC):
    def __init__(self):
        self.services = []

    @abstractmethod
    async def start_monitoring(self):
        pass


class InitMonitor(Monitor):
    def __init__(self):
        self.services = [{"service": "TEI Embedding"}]

    async def start_monitoring(self):
        pass
