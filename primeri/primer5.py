#primer1 pohlepni algoritam problme ranca
'''class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'
def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                          calories[i]))
    return menu
def greedy(items, maxCost, keyFunction):
    """Assumes items a list, maxCost >= 0,
         keyFunction maps elements of Items to numbers"""
    itemsCopy = sorted(items, key = keyFunction,
                       reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)
def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)
def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits,
               lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.density)
def maxVal(toConsider, avail): #rekurzivna funkcija
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getCost())
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result
def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)
names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 750)
print('')
testMaxVal(foods, 750)'''


#primer2 fibonaci rekurzivno koriscenjem memoizacije,dinamicko programiranje
'''n = 15
memorija = []
for i in range(n+1):
    memorija.append(0)
def fibRek(n):
    if(memorija[n] != 0):
        return memorija[n]
    if(n == 0 or n == 1):
        return 1
    memorija[n] = fibRek(n-1)+fibRek(n-2)
    return memorija[n]
print(fibRek(n))
print(memorija)'''

#primer3 fibonaci rekurzivno osnovna varijanta
'''def fib_rek(n):
    if(n==0 or n==1):
        return 1
    return fib_rek(n-1)+fib_rek(n-2)
print(fib_rek(40))'''

#primer4 fibonaci iterativno, dinamicko programiranje unapredjeno
'''a = 1
b = 1
n = 1000
for i in range(1,n):
    c = a + b
    a = b
    b = c
print(c) '''

#primer5 problem ranca unapredjen
'''class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'
def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],calories[i]))
    return menu
import random
def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items
def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total weight of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getCost())
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result
def fastMaxVal(toConsider, avail, memo = {}):
    """Assumes toConsider a list of subjects, avail a weight
         memo supplied by recursive calls
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the subjects of that solution"""
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake =\
                 fastMaxVal(toConsider[1:],
                            avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
                                                avail, memo)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    print(result[0],*result[1])
    memo[(len(toConsider), avail)] = result
    return result
def testMaxVal(foods, maxUnits, algorithm, printItems = True):
    print('Menu contains', len(foods), 'items')
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = algorithm(foods, maxUnits)
    if printItems:
        print('Total value of items taken =', val)
        for item in taken:
            print('   ', item) 
names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
#testMaxVal(foods, 750, fastMaxVal)
#for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50):
#    items = buildLargeMenu(numItems, 90, 250)
#    testMaxVal(items, 750, maxVal, False)
testMaxVal(foods, 750, fastMaxVal,True)'''


#primer6 design patterns dekorator
'''class Card:
    balance = 100
    def pay(self,amount):
        self.balance = self.balance - amount
class Visa:
    def __init__(self,card : Card):
        self.card = card
    def pay(self,amount):
        self.card.pay(amount * 1.2)
v = Visa(Card())
v.pay(10) 
print(v.card.balance) '''

#primer7 design patterns dekorator
'''class WrittenText: 
    """Represents a Written text """
    def __init__(self, text): 
        self._text = text 
    def render(self): 
        return self._text 
class UnderlineWrapper(WrittenText): 
    """Wraps a tag in <u>"""
    def __init__(self, wrapped): 
        self._wrapped = wrapped 
    def render(self): 
        return "<u>{}</u>".format(self._wrapped.render()) 
class ItalicWrapper(WrittenText): 
    """Wraps a tag in <i>"""
    def __init__(self, wrapped): 
        self._wrapped = wrapped 
    def render(self): 
        return "<i>{}</i>".format(self._wrapped.render()) 
class BoldWrapper(WrittenText): 
    """Wraps a tag in <b>"""
    def __init__(self, wrapped): 
        self._wrapped = wrapped 
    def render(self): 
        return "<b>{}</b>".format(self._wrapped.render()) 
""" main method """
if __name__ == '__main__':  #testiranje izlaza u istom fajlu, slicna je main() u javi
    before_gfg = WrittenText("GeeksforGeeks") 
    after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg))) 
 
    print("before :", before_gfg.render()) 
    print("after :", after_gfg.render()) '''

#primer8 design pattern sastav/composite
'''class LeafElement: 
    #Class representing objects at the bottom or Leaf of the hierarchy tree.
    def __init__(self, *args): 
        #Takes the first positional argument and assigns to member variable "position".
        self.position = args[0] 
    def showDetails(self): 
        #Prints the position of the child element.
        print("\t", end ="") 
        print(self.position) 
class CompositeElement: 
    #Class representing objects at any level of the hierarchy 
    # tree except for the bottom or leaf level. Maintains the child 
    # objects by adding and removing them from the tree structure.
    def __init__(self, *args): 
        #Takes the first positional argument and assigns to member 
        # variable "position". Initializes a list of children elements.
        self.position = args[0] 
        self.children = [] 
    def add(self, child): 
        #Adds the supplied child element to the list of children 
        # elements "children".
        self.children.append(child) 
    def remove(self, child): 
        #Removes the supplied child element from the list of 
        #children elements "children".
        self.children.remove(child) 
    def showDetails(self): 
        #Prints the details of the component element first. Then, 
        #iterates over each of its children, prints their details by 
        #calling their showDetails() method.
        print(self.position) 
        for child in self.children: 
            print("\t", end ="") 
            child.showDetails() 
#main method
#Whenever the Python interpreter reads a source file, 
#it does two things:
#it sets a few special variables like __name__, and then
#it executes all of the code found in the file.
#Let's see how this works and how it relates to your question about the __name__ checks we always see in Python scripts.
 
if __name__ == "__main__": 
    topLevelMenu = CompositeElement("GeneralManager") 
    subMenuItem1 = CompositeElement("Manager1") 
    subMenuItem2 = CompositeElement("Manager2") 
    subMenuItem11 = LeafElement("Developer11") 
    subMenuItem12 = LeafElement("Developer12") 
    subMenuItem21 = LeafElement("Developer21") 
    subMenuItem22 = LeafElement("Developer22") 
    subMenuItem1.add(subMenuItem11) 
    subMenuItem1.add(subMenuItem12) 
    subMenuItem2.add(subMenuItem22) 
    subMenuItem2.add(subMenuItem22) 
    topLevelMenu.add(subMenuItem1) 
    topLevelMenu.add(subMenuItem2) 
    topLevelMenu.showDetails() 
'''

#primet9 design pattern strategija
'''class Bankomat: 
    def __init__(self,balance):
        self.balance = balance
    def doPayment(self,strategy,amount):
        self.balance -= strategy.calculate(amount)
class VisaStrategy:
    def calculate(self,amount):
        return amount * 1.2
class MasterStrategy:
    def calculate(self,amount):
        return amount * 1.4
b = Bankomat(100)
b.doPayment(VisaStrategy(),10) #VisaStrategy() je bezimeni objekat
print(b.balance)
b = Bankomat(100)
b.doPayment(MasterStrategy(),10)
print(b.balance)'''


#primer10 izracunati stepen
'''total = 1
a = 3
stepen = 7
for i in range(1,stepen+1):
    total *= a
print(total)  '''






