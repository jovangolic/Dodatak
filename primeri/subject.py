#primer obesrver design pattern
from abc import ABC, abstractmethod  
 
class PenSubject(ABC):  
 
    @abstractmethod  
    def add(self, shop):  
            pass  
 
    @abstractmethod  
    def remove(self, shop):  
            pass  
 
    @abstractmethod  
    def notify(self):  
            pass  