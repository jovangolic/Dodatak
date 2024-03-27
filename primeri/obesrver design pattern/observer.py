from abc import ABC, abstractmethod  
 
 
class ShopObserver(ABC):  
 
        @abstractmethod  
        def update(self, pen):  
            pass  