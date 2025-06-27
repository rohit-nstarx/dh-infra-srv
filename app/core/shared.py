from typing import Dict
import asyncio


class ServiceStatusStore:
    _status: Dict[str, bool] = {}
    _lock = asyncio.Lock()

    @classmethod
    async def set_status(cls, service_name: str, status: bool):
        async with cls._lock:
            cls._status[service_name] = status

    @classmethod
    async def get_status(cls, service_name: str) -> bool:
        async with cls._lock:
            return cls._status.get(service_name, False)

    @classmethod
    async def get_all_statuses(cls) -> Dict[str, bool]:
        async with cls._lock:
            return dict(cls._status)  # return a copy

    @classmethod
    async def is_everything_healthy(cls) -> bool:
        async with cls._lock:
            return all(cls._status.values())
