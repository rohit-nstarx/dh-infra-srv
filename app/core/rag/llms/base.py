from abc import ABC, abstractmethod
from app.core.utils.common import ReadinessMixin


class BaseLLM(ReadinessMixin, ABC):
    @abstractmethod
    def query(self, prompt: str, **kwargs) -> str:
        """Send a query to the LLM and return the response"""
        pass
