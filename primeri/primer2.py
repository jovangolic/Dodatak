#primer 1 klasa digitron
'''class Calc:
    stat = 0
    def __init__(self):
        #self.a = a
        #self.b = b
        #self.op = op
        Calc.stat += 1
    def calc(self,a,b,op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:
                return "ne moze se deliti sa nulom"
            return a / b
        else:
            return "pogresan operator"
digitron = Calc()
d2 = Calc()      
print(digitron.calc(4,2,"+"))  
a = digitron.calc(5,0,"/") 
print(a)
print(Calc.stat)'''

#primer 2 digitron sa get i set
'''class Calc:
    def __init__(self):
        self.operand1 = 0.0
        self.operand2 = 0.0
    def add(self):
        return self.operand1 + self.operand2
    def sub(self):
        return self.operand1 - self.operand2
    def getAtribute(self):
        return self.operand1,self.operand2
    def setAtribute(self,op1,op2):
        self.operand1 = op1
        self.operand2 = op2
    def __str__(self):
        return self.operand1,self.operand2    
calc = Calc() 
calc.setAtribute(4,6)
print(calc.add()) '''


#primer 3 nasledjivanje, private,public protected
'''class Roditelj:
    def __init__(self,a,b):
        print("poziva se inicijalizator roditelja")
        self.__a = a
        self.b = b
    def _metoda1(self):
        print("poziva se metoda1")
        print(self.__a)
    def metoda2(self):
        print("poziva se metoda2 roditelja") 
        print(self.__a)   

class Dete(Roditelj):
    def __init__(self,a,b):
        print("poziva se inicijalizator deteta")
        self.a = a
        self.b = b
        super().__init__(9,7) #moze(a,b)
    def metoda2(self):
        print("poziva se metoda2 deteta")
        #print(self._a)
        #super().metoda2()

r1 = Roditelj(2,3)
#print(r1.__a)
d1 = Dete(3,4)
#print(d1._a)
r1._metoda1()
d1._metoda1()
r1.metoda2()
d1.metoda2()'''

#primer 4 get i set metode
'''class P:
    def __init__(self,x):
        self.__x = x
    def get_x(self):
        return self.__x
    def set_x(self,x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:        
            self.__x = x
p = P(1)
p.set_x(9000)
print(p.get_x())
#print(p.__x)'''

#primer5 
'''class Majka:
    def __init__(self,a):
        self.__a = a
    def pisi(self):
        print(self.__a)
m = Majka(5)
m.__a = 7
print("kopija ",m.__a)
m.pisi() '''

#primer6
'''import math
# definiše apstraktni tip koji predstavlja sve tacke u ravni
# Predstavlja tacke u ravni definisane sa x i y koord
class Tacka:
# poziva se iz konstruktora pri kreiranju objekta
    br_tacaka = 0 # klasni atribut
    t_kreiranja = None # klasni atribut
    def __init__(self, x = 0, y = 0):
        self.x = x # definisanje atributa x
        self.y = y # definisanje atributa y
        Tacka.br_tacaka += 1
# ispisuje podatke o objektu
    def predstavi_se(self):
        print('({:<.2f}, {:<f})'.format(self.x, self.y))
# racuna rastojanje do druge tacke t
    def rastojanje_do(self, t):
        dx = self.x - t.x
        dy = self.y - t.y
        return math.sqrt(dx**2 + dy**2)  
    # tekstualna reprezentacija objekta, za print(t) ili str(t)
    def __str__(self):
        return '({:<.2f}, {:<f})'.format(self.x, self.y)
    # poredi da li su dve tacke jednake
    def __eq__(self, t):
        if isinstance(t, Tacka):
            return self.x == t.x and self.y == t.y
        return False
    # sabira dva vektora definisana tackama
    def __add__(self, t):
        return Tacka(self.x + t.x, self.y + t.y)
    def __sub__(self,t):
        return Tacka(self.x - t.x, self.y - t.y)
    def __eq__(self,t):
        if isinstance(t,Tacka):
            return self.x == t.x and self.y == t.y
        return False'''


#primer7 razlomak
# najveci zajednicki delilac za prirodne brojeve x i y
'''def nzd(x, y):
    if y == 0:
        return x
    else:
        return nzd(y, x % y)
 
class Razlomak:
#Definiše razlomak zadat broijocem (a) i imeniocem (b)
# poziva se iz konstruktora pri kreiranju razlomka
    def __init__(self, a, b):
        try:
            a, b = int(a), int(b)
        except:
            raise Exception('uneti brojevi nisu celobrojni!')
        if b == 0:
            raise Exception('imenilac je 0')
        else:
            if (a < 0 and b > 0) or (a > 0 and b < 0):
                a = - abs(a)
            else:
                a = abs(a)
                b = abs(b)
        k = nzd(abs(a), b)
        self.a = a // k
        self.b = b // k
# tekstualna reprezentacija razlomka
    def __str__(self):
        return '{:<d}/{:<d}'.format(self.a, self.b)
# vraca realnu vrednost
    def vrednost(self):
        return self.a / self.b
# redefinisanje operacije +
    def __add__(self, r):
        return Razlomak(self.a * r.b + r.a * self.b,self.b * r.b)
# redefinisanje operacije -
    def __sub__(self, r):
        return Razlomak(self.a * r.b - r.a * self.b,self.b * r.b)
# redefinisanje operacije *
    def __mul__(self, r):
        return Razlomak(self.a * r.a, self.b * r.b)
# redefinisanje operacije /
    def __truediv__(self, r):
        return Razlomak(self.a * r.b, r.a * self.b)
x = Razlomak(-3,5)
y = Razlomak(5,3)
print("{} + {} = {}".format(x,y, x+y))
print("{} - {} = {}".format(x,y, x-y))
print("{} * {} = {}".format(x,y, x*y))
print("{} / {} = {}".format(x,y, x/y))'''

#primer8 
# predstavlja sve osobe u informacionom sistemu fakulteta
'''class Osoba:
    def __init__(self, ime, prezime, jmbg):
        self.__ime = ime
        self.__prezime = prezime
        self.__jmbg = jmbg
    def __str__(self):
        return '{} {} {}'.format(self.__ime, self.__prezime,self.__jmbg)
    def predstavi_se(self):
        print('Ja sam', self.__ime, self.__prezime)
# predstavlja osobe zaposlene na fakultetu
class Zaposleni(Osoba): # izvodjenje iz klase Osoba
    def __init__(self, ime, prezime, jmbg, plata, soba, telefon):
        super().__init__(ime, prezime, jmbg) # priroda osobe
        self.__plata = plata
        self.__soba = soba
        self.__telefon = telefon
 
    def __str__(self):
        return super().__str__() + '\n' + str(self.__plata) + \
            ' soba: ' + self.__soba + ' tel: ' + self.__telefon
 
    def promeni_platu(self, nova):
        self.__plata = nova
# predstavlja studente na fakultetu
class Student(Osoba): # izvodjenje iz klase Osoba
    def __init__(self, ime, prezime, jmbg, indeks, smer):
        super().__init__(ime, prezime, jmbg) # priroda osobe
        self.__indeks = indeks
        self.__godina = 1
        self.__smer = smer
    def __str__(self):
        return super().__str__() + '\n' + self._indeks + \
            ' godina: ' + str(self.__godina) + ' smer: ' + self.__smer
 
    def upisi_godinu(self, godina):
        if godina < 6 and (godina == self.__godina or # max 5 god
                           godina == self.__godina + 1):
            self.__godina = godina
#import Osoba as f
z = Zaposleni('Aca', 'Vukic', '12153', 95000, '3a', '4218-589')
s = Student('Mitar', 'Miric', '12131', '119/17', 'MTI')
print(isinstance(s, Student), isinstance(s, Osoba))
z.predstavi_se()
s.predstavi_se()
print(z)'''

#primer 9 zgrada
# definiše apstraktni tip koji predstavlja vlasnike stanova
'''class Vlasnik:
    def __init__(self, ime, prezime, jmbg):
        self.__ime = ime
        self.__prezime = prezime
        self.__jmbg = jmbg
    def __str__(self):
        return '{} {} {}'.format(self.__ime,self.__prezime, self.__jmbg)
    def jmbg(self):
        return self.__jmbg
# da li ime ili prezime sadrži kljucnu rec
    def ime_sadrzi(self, upit):
        ime_ok = self.__ime.find(upit) != -1
        prezime_ok = self.__prezime.find(upit) != -1
        return ime_ok or prezime_ok
# definiše tip koji predstavlja stanove
class Stan:
    def __init__(self, m2, sprat):
        self.__m2 = m2
        self.__sprat = sprat
        self.__vlasnik = None
    def __str__(self):
         st = '{}m2 spr. {}'.format(self.__m2, self.__sprat)
         return '{}. {}'.format(st, str(self.__vlasnik))
    def vlasnik(self):
        return self.__vlasnik
    def promeni_vlasnika(self, novi_vlasnik):
        self.__vlasnik = novi_vlasnik
    def površina(self):
        return self.__m2  
class Zgrada:
    def __init__(self, adresa, stanovi):
        self.__adresa = adresa
        self.__stanovi = stanovi
    def __str__(self):
        opis = []
        for stan in self.__stanovi:
            opis.append(str(stan))
        return '{}\n---\n{}\n---\n'.format(self.__adresa, opis)
    def dodaj_stan(self, stan):
        self.__stanovi.append(stan)
# vraca recnik sa vlasnicima koji zadovoljavaju upit
# i njihovim stanovima
    def stanovi_vlasnika(self, upit):
        vlasnik_stanovi = {} # recnik sa stanovima po vlasniku
        for stan in self.__stanovi:
            v = stan.vlasnik()
            if v != None and v.ime_sadrzi(upit):
                v_stanovi = vlasnik_stanovi.get(v.jmbg(), [])
                v_stanovi.append(stan)
                vlasnik_stanovi[v.jmbg()] = v_stanovi
        return vlasnik_stanovi      
v1 = Vlasnik('Dragan',"Torbica","12434353")
v2 = Vlasnik("Djordje","Cvarkov","13430244")
s1 = Stan(100,0)
s2 = Stan(56,0)
s3 = Stan(78,1)
s4 = Stan(80,1)
z1 = Zgrada("Bulevar Oslobodjenja",[s1,s2,s3,s4])
print(z1)
s5 = Stan(45,2)
z1.dodaj_stan(s5)
print(z1)
print(z1.stanovi_vlasnika("Dragan"))'''


#primer10 lambda i map
'''n1 = [1,2,3]
n2 = [4,5,6]
rez = map(lambda x,y : x+y,n1,n2)
#print(list(rez))
print(set(rez))'''


#primer11 nasledjivanje vezba
'''from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name 
    @abstractmethod
    def calculate_payroll(self):
        pass    
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
    def calculate_payroll(self):
        return self.weekly_salary        
class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name) 
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission
    def calculate_payroll(self):
        fixed = super().calculate_payroll() # dovoljno je promeniti calculate_payroll() u nadklasi
        return fixed + self.commission
class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees: # svi su employees
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')
#import hr
salary_employee = SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])
print("-----------------------------------")
employees = [
    salary_employee,
    hourly_employee,
    commission_employee
]
for emp in employees:
    print(emp.calculate_payroll())'''

#primer12 hestabela hashtable
'''class HashTable:
    def __init__(self):
        self.__data = [0] * 100
        self.__len = len(self.__data) 
    def add(self, key, value):
        index = id(key)%self.__len
        self.__data[index] = value
    def get(self,key):
        index = id(key)%self.__len
        return self.__data[index] 
    def __str__(self):
        return str(self.__data)
ht = HashTable()
print(ht)
print(id("my_key"))
ht.add("my_key","Hello!")
ht.add("my_key_1","World")
print(ht)
print(ht.get("my_key_1"))'''


#primer13 povezane liste
'''class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print ("-->",printval.dataval,end=" ")
            printval = printval.nextval 
    def atBeginning(self,data):
        new_node = Node(data)
        new_node.nextval = self.headval  
        self.headval = new_node     
    def atEnd(self,data):
        new_node = Node(data)
        n = self.headval
        while n.nextval is not None:
            n = n.nextval
        n.nextval = new_node
        n = new_node
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
# Function to remove node
    def RemoveNode(self, Removekey):
        HeadVal = self.head
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        if (HeadVal == None):
            return
        prev.next = HeadVal.next
        HeadVal = None             
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thr")
# Link first Node to second node
list.headval.nextval = e2
# Link second Node to third node
e2.nextval = e3 
e3.nextval = e4
list.atBeginning("Sun")
list.atEnd("trii")
list.listprint()       '''


#primer14  binarno stablo
'''class Node:
    def __init__(self, data):
 
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data,end=" ")
        if self.right:
            self.right.PrintTree()
    def lrr(self):
        if self.left:
            self.left.lrr() 
        if self.right:
            self.right.lrr() 
        print(self.data,end=" ")
    def rootLeftRight(self):
        print(self.data,end=" ")
        if self.left:
            self.left.rootLeftRight()
        if self.right:
            self.right.rootLeftRight()                      
# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(13)
root.insert(15)
root.insert(14)
root.insert(3)
root.PrintTree()
root.lrr()
root.rootLeftRight()'''


#primer14 regularni izrazi
'''import re
txt = "The rain in Spain"
x = re.findall("ai",txt)
print(x)'''

#primer15 regularni izrazi telefonski broj
'''import re
p = re.compile("^\(\d{3}\)-\d{4}-\d{3}$")
print(p.search("(011)-4562-345"))'''


#primer16 design pattern observer
'''class Resevoir:
    def __init__(self):
        self.reserveLimit = 10
        self.totalAmount = 100
    def reserveIndicator(self):
        print("hey, i am on reserve! Please refill me.") 
    def getFuel(self):
        self.totalAmount -= 1
        if self.totalAmount <= self.reserveLimit:
            self.reserveIndicator()
        print(self.totalAmount)           
res = Resevoir() 
for i in range(100):
    res.getFuel() '''
'''import time
import abc
class EventListener(abc.ABC):
    @abc.abstractmethod
    def reserve_reached(self,sender):
        pass
 
class MyListener(EventListener):
    def reserve_reached(self, sender):
        print("No more fuel in car. Please refill!")
    def __str__(self):
        return "ja sam osluskivac..."   
 
class Reservoir:
    def __init__(self):
        self.current_state = 100
        self.reserve_limit = 50
        self.listeners = []  
    def add_listener(self, listener):
        self.listeners.append(listener)
    def remove_listener(self, listener):  
        self.listeners.remove(listener)
    def ispisiOsluskivace(self):
        for listener in self.listeners:
            if isinstance(listener,EventListener) :
                print(listener)   
    def distribute_event(self):
        for listener in self.listeners:
            if isinstance(listener, EventListener):
                listener.reserve_reached(self)   
    def consume_fuel(self):
        print(f"Fuel consumed. {self.current_state} liters remaining")
        self.current_state -= 1
        if self.current_state < self.reserve_limit:
            self.distribute_event() 
res = Reservoir() 
res.add_listener(MyListener())
res.add_listener(MyListener())
m = MyListener()
res.add_listener(m)
res.ispisiOsluskivace()
for i in range(0,100):
    res.consume_fuel()
    time.sleep(0.1)   '''


#primer17 singleton design pattern
'''class Singleton:
   __instance = None
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self
#s = Singleton()
#print(s)
s = Singleton.getInstance()
print(s)
s = Singleton.getInstance()
print(s)'''

#primer18 rad sa datotekama


