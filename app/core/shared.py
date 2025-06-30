from typing import Dict
from collections import deque
import asyncio


class ServiceStatusStore:
    _status: Dict[str, deque] = {}
    _lock = asyncio.Lock()
    _history_limit = 3

    @classmethod
    async def set_status(cls, service_name: str, status: bool):
        async with cls._lock:
            if service_name not in cls._status:
                cls._status[service_name] = deque(maxlen=cls._history_limit)
            cls._status[service_name].append(status)

    @classmethod
    async def get_status(cls, service_name: str) -> bool:
        async with cls._lock:
            history = cls._status.get(service_name, deque(maxlen=cls._history_limit))
            return list(history).count(True) >= 2

    @classmethod
    async def get_all_statuses(cls) -> Dict[str, bool]:
        print(cls._status)
        async with cls._lock:
            return {
                name: (list(history).count(True) >= 2)
                for name, history in cls._status.items()
            }

    @classmethod
    async def is_everything_healthy(cls) -> bool:
        async with cls._lock:
            return all(
                list(history).count(True) >= 2
                for history in cls._status.values()
            )
