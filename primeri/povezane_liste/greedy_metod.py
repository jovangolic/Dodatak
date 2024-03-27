#greedy metod - pohlepni algoritam problem ranca
'''class Food:
    def __init__(self,n,v,w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue() / self.getCost()
    def __str__(self):
        return self.name+": <"+str(self.value)+", "+str(self.calories)+">"
def build_menu(names,values,calories):
    menu = []
    for i in range(len(names)):
        menu.append(Food(names[i],values[i],calories[i]))
    return menu
def greedy(items,maxCost,keyFunction): #items je lista,maxCost >=0,keyFunction mapira elemente items u brojeve
    lista = sorted(items,key=keyFunction,reverse=True) #nova lista koja je sortirana tj. to je kopija items liste
    result = []
    totalValue,totalCost = 0.0,0.0
    for i in range(len(lista)): 
        if(totalCost+lista[i].getCost()) <= maxCost: #uporedjujem po kalorijama
            result.append(lista[i])
            totalCost += lista[i].getCost()
            totalValue += lista[i].getValue()
    return (result,totalValue)              #npr maxCost mora biti <= 750      
def test_greedy(items,constraint,keyFunction):
    taken,val = greedy(items,constraint,keyFunction)
    print("total values of items taken =", val) #taken je result, val je totalValue (result,totalValue)
    for item in taken: #iteracija za taken
        print("  ", item)  
def testGreedys(foods,maxUnit): #foods predstavlja klasu Food(),maxUnit je granicnik npr do 750 kalorija
    print("\ntestiranje po vrednostima - values ", maxUnit," kalorije")
    test_greedy(foods,maxUnit,Food.getValue)
    print("\ntestiranje po kalorijama: ",maxUnit," kalorije")
    test_greedy(foods,maxUnit,lambda x: 1/Food.getCost(x))  
    print("\ntestiranje po gustini / density: ",maxUnit," kalorije")
    test_greedy(foods,maxUnit,Food.density)      
def maxVal(lista,granicnik): #rekurzivno
    if lista == [] or granicnik == 0:
        result = (0,())
    elif lista[0].getCost() > granicnik:
        result = maxVal(lista[1:],granicnik) #pregledanje samo desne grane
    else:
        nextItem = lista[0] 
        # pregledanje leve grane
        withVal,withToTake = maxVal(lista[1:],granicnik - nextItem.getCost())
        withVal += nextItem.getValue()
        #pregledanje desne grane
        withoutVal,withoutToTake = maxVal(lista[1:],granicnik)
        if withVal > withoutVal:
            result = (withVal,withToTake + (nextItem,))
        else:
            result = (withoutVal,withoutToTake)
    return result
def testMaxVal(food,maxUnit,printItems = True):
    print("use search tree to allocate ",maxUnit," calories")
    val,taken = maxVal(food,maxUnit)
    print("total values of items taken =",val)
    if printItems:
        for item in taken:
            print("  ",item)                

names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10,82]
calories = [123,154,258,354,365,150,95,195,202]
foods = build_menu(names,values,calories)
testGreedys(foods,750)
print()
testMaxVal(foods,750)'''


              