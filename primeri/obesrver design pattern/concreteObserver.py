from observer import ShopObserver  
from concreteSubject import Pen  
 
 
class Shop(ShopObserver):  
 
        def __init__(self, shopName: str):  
            self._shopName = shopName  
 
        def update(self, pen: Pen):  
            print("pen prize changed to ", pen.penPrize, ' in ', self._shopName)  