#iks-oks program
'''print("Kratak opis: Igra je za dva igraca, Igrac br. 1 je X, i, Igrac br.2 je O")    
print("Napomena: Polja na IKS-OKS tabeli su numerisana kao na desnoj strani tastature koja je odredjena za racunske operacije.")
print("Polozaj broja na tastaturi odgovara polozaju vaseg odigranog poteza na dijagramu igre.")
fields = {"7":" ","8":" ","9":" ","4":" ","5":" ","6":" ","1":" ","2":" ","3":" "}
field_keys = []
for key in fields:
    field_keys.append(key)
def board(polje): #kreiranje table za igru
    print(polje["7"] + "|" + polje["8"] + "|" + polje["9"])
    print("-+-+-")
    print(polje["4"] + "|" + polje["5"] + "|" + polje["6"])
    print("-+-+-")
    print(polje["1"] + "|" + polje["2"] + "|" + polje["3"])    
def game():
    korak = "X"
    brojac = 0
    for i in range(10): # za 10 tabli
        board(fields)
        print("Sada si ti na potezu," + korak + ". Koje polje zelis da izaberes?")
        potez = input() 
        if fields[potez] == " ":
            fields[potez] = korak
            brojac += 1
        else:
            print("To polje je vec zauzeto. Izaberi drugo polje.")
            continue
        if brojac >= 5:
            if fields["7"] == fields["8"] == fields["9"] != " ":
                board(fields)
                print("\nKraj igre.\n")
                print(" **** "+korak+" je pobedio. ****")
                break
            elif fields["4"] == fields["5"] == fields["6"] != " ":
                board(fields)
                print("\nKraj igre.\n")
                print(" **** "+korak+" je pobedio. ****")
                break       
            elif fields["1"] == fields["2"] == fields["3"] != " ":
                board(fields)
                print("\nKraj igre.\n")
                print(" **** "+korak+" je pobedio. ****")
                break
            elif fields["7"] == fields["4"] == fields["1"] != " ":
                board(fields)
                print("\nKraj igre.\n")
                print(" **** "+korak+" je pobedio. ****")
                break
            elif fields["8"] == fields["5"] == fields["2"] != " ":
                board(fields)
                print("\nKraj igre.\n")
                print(" **** "+korak+" je pobedio. ****")
                break
            elif fields["9"] == fields["6"] == fields["3"] != " ":
                board(fields)
                print("\nKraj igre.\n")
                print(" **** "+korak+" je pobedio. ****")
                break
            elif fields["7"] == fields["5"] == fields["3"] != " ":
                board(fields)
                print("\nKraj igre.\n")
                print(" **** "+korak+" je pobedio. ****")
                break
            elif fields["9"] == fields["5"] == fields["1"] != " ":
                board(fields)
                print("\nKraj igre.\n")
                print(" **** "+korak+" je pobedio. ****")
                break
        if brojac == 9:
            board(fields)
            print("\nKraj igre.\n") 
            print("IGRA JE NERESENA!!!!!!!")
        if korak == "X" : #sledeci korak postaje O
            korak = "O"
        else:
            korak = "X"          
    restart = input("Da li zelite da pocnete novu igru(y/n)?")
    if restart == "y":
        for i in field_keys:
            fields[i] = " "
        game()
    else:
        print("\nIgra je gotova.KRAJ")
        exit()            
if __name__ == "__main__":
    game()    '''


#deo saha,figura skakac
'''start = [int(input("x: ")), int(input("y: "))]
slova = ["A","B","C","D","E","F","G","H"]
available = [[start[0]-1,start[1]-2],
             [start[0]-2,start[1]-1],
             [start[0]+1,start[1]-2],
             [start[0]+2,start[1]-1],
             [start[0]-1,start[1]+2],
             [start[0]-2,start[1]+1],
             [start[0]+1,start[1]+2],
             [start[0]+2,start[1]+1]]
print(available)
used_positions = 0
for y in range(8):
    print(y+1,end=" ")
    for x in range(8):
        chr = "O"
        if[x+1,y+1] == start:
            chr = "S"
        if[x+1,y+1] in available:
            used_positions += 1
            chr = "M"
        print(chr,end="")
    print()
print(end=" ")
for s in slova:
    print(s,end=" ")
print()
print("possible positions: ",used_positions)       '''


#fibonaci rekurzivno sa pamcenjem(dinamicko programiranje)
'''num = int(input("unesi broj: "))
memorija = []
for i in range(num+1):
    memorija.append(int(0))
def fibonaci_rec(n):
    if memorija[n] != 0:
        return memorija[n]
    if n == 0 or n == 1:
        return 1
    memorija[n] = fibonaci_rec(n-1)+fibonaci_rec(n-2)
    return memorija[n]
#print(fibonaci_rec(num))'''
#fibonaci iterativno sa pamcenjem(dinamicko programiranje)
'''def fibonaci_iter(n):
    a,b = 0,1
    suma = 0
    for i in range(n):
        if i < n:    
            suma = a+b
            a = b
            b = suma
    return suma
print(fibonaci_iter(10))       '''

#fibonaci sa rekurzijom koji vraca listu brojeva
def fibonaci(n,lista=[]): 
    if n == 0: #vraca praznu listu
        return lista 
    else:
        if len(lista) < 2: #u listu se dodaje broj 1; izlaz je: [1]
            lista.append(1)
            fibonaci(n-1,lista)
        else:
            last = lista[-1]
            second_last = lista[-2]
            lista.append(last+second_last)
            fibonaci(n-1,lista)
        return lista
#print(fibonaci(500))       

#npr rekurzija
low = 1
high = 5       
def recTest(l,h):
    if l > h:
        return 
    print(l,end=" ")
    recTest(l+1,h)
#recTest(low,high)  
def recTest2(l,h):
    if l <= h:
        print(l,end=" ")
        recTest2(l+1,h)      
#recTest2(low,high)      

#generatori
'''import time
def odd_gen(n,m):
    while n < m:
        yield n
        n+=2
def odd_lists(n,m):
    l = []
    while n < m:
        l.append(n)
        n+=2
    return l
t1 = time.time()
print(sum(odd_gen(1,10)))
print("vreme da sabere gen: %f"%(time.time() - t1))
t1 = time.time()
print(sum(odd_lists(1,10)))
print("vreme da sabere list: %f"%(time.time()-t1))  '''

#npr rad sa fajlom
'''def word_count(fajl):
    try:
        file = open(fajl)
    except:
        print("dati fajl ne postoji")
        exit()   
    count = dict()
    for line in file:
        words = line.split() 
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    return count
brojac = word_count("alice.txt")
print(brojac)                
trazi = [(k,v) for k,v in brojac.items() if v >=4]
print(trazi)'''


#npr chainMap
'''from collections import ChainMap
d1 = {"a":1,"b":2,"c":3}
d2 = {"c":3,"d":4}
d3 = {"e":5,"f":6}
chain = ChainMap(d1,d2,d3)
print(chain)
c = chain.maps
c2 = chain.keys()
c3 = chain.values()
print(c2)
print(c3)
print(c)'''

#npr collections
'''import collections
d1 = {"a":1,"b":2}
d2 = {"b":3,"c":4}
#inicijalizacija ChainMap
chain = collections.ChainMap(d1,d2)
#prikaz chanimap koristeci maps
print("all the chanmap contents are: ")
print(chain.maps)
#stampanje kljuceva koristeci keys()
print("all keys of chainmap are: ")
print(chain.keys())
#stampanje vrednosti koristeci values()
print("all values of chainmap are: ")
print(chain.values())'''

'''import collections
dic1 = { 'a' : 1, 'b' : 2 } 
dic2 = { 'b' : 3, 'c' : 4 } 
dic3 = { 'f' : 5 }
chain = collections.ChainMap(dic1,dic2)
print(chain.maps)
ch1 = chain.new_child(dic3)
print("nova chainmap:")
print(ch1.maps)
print("value associated with b before reversing is: ",end="")
print(ch1["b"]) # za prvo b:2 stampa od leva prema desno, prvo ponavljanje
ch1.maps = reversed(ch1.maps)
print("value associated with b before reversing is: ",end="")
print(ch1["b"]) #za drugo b:3 stampa od desna prema levo, prvo ponavljanje sa desne strane'''

#npr container
from collections import Counter
#with sequence of items
#print(Counter(["B","B","A","B","C","A","B","B","A","C"]))
#with dictionary
#print(Counter({"A":3,"B":5,"C":2}))
#with keyword arguments
#print(Counter(A=3,B=5,C=2))


'''l = ["B","B","A","B","C","A","B","B","A","C"]
def counter(num):
    d = {}
    for i in num:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d
print(counter(l)) '''

#from collections import Counter
'''count = Counter()
count.update([1,2,3,1,2,1,2])
print(count)
count.update([1,2,4])
print(count)'''

#oduzimanje
'''from collections import Counter
c1 = Counter(A=4,B=3,C=10)
c2 = Counter(A=10,B=3,C=4)
c1.subtract(c2)
print(c1)'''


#from collections import Counter
#l = ["blue","red","blue","yellow","blue","red"]
#print(Counter(l)) #napravio se bezimeni objekat

#npr za orderedDict; pamti redosled umetnutih kljuceva
#from collections import OrderedDict
'''print("this is a dict:\n")
d = {}
d["a"] = 1
d["b"] = 2
d["c"] = 3
d["d"] = 4
print(d)
for k,v in d.items():
    print(k,v)
print("\nThis is an OrderedDict:\n")
od = OrderedDict()    
od["a"] = 1
od["b"] = 2
od["c"] = 3
od["d"] = 4
for k,v in od.items():
    print(k,v)'''

#npr promena vrednosti u orderedDict-u
'''print("before:\n")
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
od["d"] = 4
for k,v in od.items():
    print(k,v)
print("after:\n")
od["c"] = 5
for k,v in od.items():
    print(k,v)'''

#Deletion and Re-Inserting: Deleting and re-inserting the same key will push it to the back as OrderedDict
#however maintains the order of insertion.
'''from collections import OrderedDict
print("before deleting:\n")
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
od["d"] = 4
for k,v in od.items():
    print(k,v)
print("after deleting:\n")
od.pop("c")
for k,v in od.items():
    print(k,v)
print("\nafter re-inserting:\n") 
od["c"] = 3       
for k,v in od.items():
    print(k,v)'''

#npr namedtuple
'''from collections import namedtuple
Student = namedtuple("Student",["name","age","DOB"]) #deklarisanje namedtuple-a
S = Student("Milica","19","2541997") #dodavanje vrednosti
print("the student age using index is: ",end="")
#print(S)
print(S[1]) #pristupanje indeksu
print()
print("the student name using keyname is: ",end="")
print(S.name)'''

#access operations
'''import collections
student = collections.namedtuple("Student",["name","age","DOB"])
s = student("nandini","19","27121999")
print("student age using index is: ",end="")
print(s[1])
print("student name using keyname is: ",end="")
print(s.name)
print("student dob using getattr() is: ",end="")
print(getattr(s,"DOB"))'''

#conversation operations sa _make(),_asdict(), "**"operatorom, koristeci namedtuple()
'''import collections
student = collections.namedtuple("Student",["name","age","DOB"])  #deklarisanje nametuple
s = student("nandini","19","27121999")  #dodavanje vrednosti
lst = ["manjeet","19","411997"]  # inicijalizacija iterablea
d1 = {"name":"nikhil","age":19,"DOB":"1391997"}  #inicijalizacija recnika
print("namedtuple instance using iterable : ")  #koriscenje _make()
print(student._make(lst))
print("orderedDict instance uisng namedtuple: ")  #koriscenje _asdict()
print(s._asdict()) # _asdict() kao argument zahteva objekat
print("namedtuple instance from dict is: ")  #koriscenje operatora **
print(student(**d1))'''

#additional operations sa _fields(), _replace()
'''import collections
student = collections.namedtuple("Student",["name","age","DOB"])
s = student("milica","19","27121997")
print("all the fields of students are: ") #koriscenje _fields()
print(s._fields)
print("the modified namedtuple is : ") #koriscenje _replace()
print(s._replace(name="milica"))'''




