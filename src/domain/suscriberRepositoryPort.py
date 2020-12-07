from abc import ABC, abstractmethod

class SuscriberRepository(ABC):

    @abstractmethod
    def save(self,suscriber):
       pass

    @abstractmethod
    def getAll(self) -> list:
        pass
    
    @abstractmethod
    def delete(self, topic_name) -> int:
        pass
    
    @abstractmethod
    def searchByTopic(self, topic_name) -> dict:
        pass