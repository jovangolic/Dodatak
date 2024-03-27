from concreteObserver import Shop  
from concreteSubject import Pen  
 
pen = Pen(10)  
pen.add(Shop('Shop1'))  
pen.add(Shop('Shop2'))  
pen.add(Shop('Shop3'))  
 
pen.penPrize = 15  
pen.penPrize = 20  
pen.penPrize = 32  