from subject import PenSubject  
 
 
class Pen(PenSubject):  
 
        def __init__(self, prize):  
            self._penPrize = prize  
 
        shops = []  
 
        def add(self, shop):  
            self.shops.append(shop)  
 
        def remove(self, shop):  
            self.shops.remove(shop)  
 
        def notify(self):  
            for shop in self.shops:  
                shop.update(self)  
            print('---------------------------------------')  
 
        @property  
        def penPrize(self):  
            return self._penPrize  
 
        @penPrize.setter  
        def penPrize(self, prize):  
            self._penPrize = prize  
            self.notify()  