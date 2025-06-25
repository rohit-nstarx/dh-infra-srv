from abc import ABC, abstractmethod

class BaseLLM(ABC):
    def __init__(self):
        self.client = None        

    @abstractmethod
    def query(self, prompt: str, **kwargs) -> str:
        """Send a query to the LLM and return the response"""
        pass
    
    @abstractmethod
    def get_available_models(self) -> List[str]:
        """Get list of available models for this provider"""
        pass
    


    
