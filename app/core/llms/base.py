from abc import ABC, abstractmethod
from typing import List


class BaseLLM(ABC):
    @abstractmethod
    def is_ready(self) -> bool:
        pass

    @abstractmethod
    def query(self, prompt: str, **kwargs) -> str:
        """Send a query to the LLM and return the response"""
        pass

    