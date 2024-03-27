
"""num2 = input("unesi prvi broj: ")
num1 = input("unesi drugi broj: ")
if(num1 > num2):
    max1 = num1
else:
    max1 = num2
print("max je: ",max1)        
"""

"""num1 = float(input("unesi prvi broj: "))
num2 = float(input("unesi drugi broj: "))  
sabiranje = num1 + num2
oduzimanje = num1 - num2
deljenje = num1 / num2
mnozenje = num1 * num2
print("sabiranje je ",sabiranje)
print("oduzimanje je ",oduzimanje)
print("deljenje je ",deljenje)
print("mnozenje je ",mnozenje)"""


#primer 1
'''import random
highscore = random.randint(0,100)
lastscore = highscore
userscore = int(input('unesi svoj ucinak: '))
if(userscore > lastscore):
#f(userscore > highscore):
    userscore = highscore
    #print('cestitka. you beat thi high score ',userscore)
    print('cestitka. you beat thi high score ',lastscore)
else:
    print('failed') 
print('highscore ',highscore)   '''


#primer 2
'''par = 0
nep = 0
for i in range(1,101):
    if(i % 2 == 0):
        par += i
    else:
        nep += i
print("zbir parnih je: ",par,"\n zbir neparnih je ",nep)     '''

#primer 3
'''k = 2010
for i in range(6):
    print(k + i)
'''

# primer crtanje prozora
'''for i in range(5):
    for j in range(5): 
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("#",end=" ")
        else:
            print(" ",end=" ")    
    print()    

#primer5 crtanje iksa
for i in range(5):
    for j in range(5):
        if i == j or j+i == 4:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()            '''

#primer 6 crtanje prozora sa iksom
'''n = 10
for i in range(n+1):
    for j in range(n+1):
        if(i==0 or i ==n or j==0 or j==n or i == j or j+i == n):
            print("#",end="")
        else:
            print(" ",end="")    
    print()        '''


#primer 7 crtanje trougla
'''for i in range(20):
    #f(i<10):
    #    pom = i+1
    #else:
    #    pom = 20 - i - 1 
    #pom = i+1 if(i<10) else  20-i-1  
    for j in range(pom):
        print("*",end="")  
    print() '''


#primer 8
'''ind = True
for i in "banana":
    print(i, end="")
    if(i=="a"):
        if(ind==False):
            break
        else:
            ind = False'''

#primer 9 ispis parnih brojeva koristeci continue
'''l = [1,2,3,4,5,6,7,8,9,10]
for i in l:
    if i %2 ==1:
        continue
    print(i)'''


#primer 10
'''a = [7,15,9]
zbir1 = 0
zbir2 = 0
for i in range(len(a)):
    #print(a[len(a) - i -1]) ispisuje od zadnjeg
    #zbir1 += a[i]
    if(i%2 ==0):
        zbir1 += a[i]
for i in a:
    zbir2 += i    
print(zbir1)  
print(zbir2)  '''


#primer 11 pretvaranje stringa u listu,kvadriranje brojeva i vracanje u string
'''s1 = ""
l = []
for i in "2345":
    l.append(int(i))
#print(l)
for i in l:   
    print(i*i)
    s1 += str(i*i)
print(s1)'''

#pretvaranje liste int u string
'''l1 = [1,2,3]
s = "".join(str(i) for i in l1)
print(s)'''

#pretvaranje liste stringova u string
'''l = ["a","b","c"]
s = "".join(l)
print(s)
print(type(s))     '''


#primer 12 obrnuti niz
'''l = [7,4,10,5,1,9]
#prvi nacin
#for i in range(len(l)-1,-1,-1):
#    print(l[i],end=",")
#drugi nacin
n = len(l)
for i in range(n//2):
    pom = l[i]
    l[i] = l[n-1-i]
    l[n-1-i] = pom
print(l)  '''

#primer 13 sortiranje niza u rastucem poretku
#trebaju nam 2 petlje
'''a = [7,4,10,5,1]
n = len(a)
for i in range(n-1):
    for j in range(i+1,n):
        if(a[i] > a[j]):
            a[i],a[j] = a[j],a[i]
            #pom = a[i]
            #a[i] = a[j]
            #a[j] = pom
print(a)'''

#primer 14 sabiranje 2 liste
'''a = [1,2,3]
b = [4,5,6]
c = []
for i in range(len(a)):
    c.append(a[i] + b[i])
print(c) '''


#primer15 par, nepar liste
'''a = [3,7,1,9,2,4,5,12]
par = []
nep = []
for i in range(len(a)):
    if(a[i] % 2 ==0):
        par.append(a[i])
    else:
        nep.append(a[i])
print(par)
print(nep) '''

#primer 16 sabiranje 2 matrice
'''A = [[2,4,5],[1,3,7],[6,2,8]]
B = [[1,3,1],[8,9,7],[5,3,2]]
c = []
for i in range(len(A)):
    c.append([A[i][0]+B[i][0],A[i][1]+B[i][1],A[i][2]+B[i][2]])
print(c)  '''

#primer 17 mnozenje 2 matrice
'''a = [1,2]
b = [[3,4],[5,6]]
c = []
c.append([a[0]*b[0][0] + a[1]*b[1][0] , a[0]*b[1][0] + a[1]*b[1][1]])
print(c) '''

#primer 18 pravljenje matrice
'''r = int(input('unesi broj redova: '))
c = int(input("unesi broj kolona: "))
matrix = []
for i in range(r):
    a = []
    print("unesi red: ")
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()   '''


#primer 19 pravlenje slucajne matrice
'''import random
a = []
for i in range(10):
    a.append([])
print(a)
for i in range(10):
    random.seed(i)
    for j in range(10):
        a[i].append(random.randint(1,10))
for i in range(10):
    print(a[i],end=" ")        
    print()'''

#primer 20 torka
'''person = (15,"peter","jackson",35)
ids,fisrt,last,age = person
print(ids)
print(fisrt)
for p in person:
    print(p,end=",") '''


#primer 21 funkcija koja racuna faktorijel
'''def fact(n):
    if n == 0:
        return 1
    total = 1
    for i in range(1,n+1):
        total *= i
    return total
def ispisFaktorijele(n):
    for i in range(n+1):
        print(fact(i))
ispisFaktorijele(10)  '''

#primer22 sabiranje 2 liste
'''niz1 = [1,2,3]
niz2 = [4,5,6]
def zbir(n1,n2):
    c = [0,0,0]
    for i in range(len(n1)):
        c[i] = n1[i]+n2[i]
    return c
print(zbir(niz1,niz2)) '''


#primer 23 rekurzija
'''def rec(n):
    if(n>0):
        print(n-1)
        rec(n-1)
rec(5)'''


#primer 24 rekurzija
'''def rec(n):
    if(n==0):
        return
    print(n-1)
    rec(n-1)
rec(5)    '''

#primer 25 rekurzija
'''def rec(n):
    if(n==0):
        return
    rec(n-1)
    print(n-1)
rec(5) '''

#primer 26 rekurzija
'''def f(n):
    if(n==0):
        return
    print(n-1)
    f(n-1)
    print(n-1)
f(5) '''

#primer 27 sabiranje preko rekurzije
'''def recZbri(n):
    if(n == 0):
        return 0
    return n+ recZbri(n-1)
print(recZbri(5))'''

#primer 28 faktorijel iterativno
'''def factIter(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    return total
print(factIter(5))  '''

#primer 29 faktorijel rekurzivno
'''def factRec(n):
    if(n == 1):
        return 1
    return n * factRec(n-1)
print(factRec(5))'''

#primer 30 binarni prikaz brojeva iterativno
'''for i in range(2):
    for j in range(2):
        for k in range(2):
            print(i,j,k)'''

#primer 31 binarni prikaz brojeva rekurzivno, backtracking
'''n = 3
nizovi = []
x = []
for i in range(n):
    x.append(0)
#print(x)
def rek(l):
    print("poziva se rek(",l,")")
    if(l == n):
        print(x)
        nizovi.append(x.copy())
    else:
        x[l] = 0
        rek(l+1)
        x[l] = 1
        rek(l+1)
rek(0)  
print(nizovi) '''

#primer 32 prolaz kroz niz rekurzivno
'''niz = [9,7,3,5]
def prolaz(i):
    if(i < len(niz)):
        print(niz[i],end=" ")
        prolaz(i+1)
prolaz(0)
def prolaz2(i):
    if(i==len(niz)):
        return
    print(niz[i],end=" ")
    prolaz2(i+1)
prolaz2(0)  '''

#primer 33 pravljenje steka sa rekurzijom
'''niz = []
n = 5
def dodajIispisi(i):
    if(i==n):
        return
    niz.append(i)
    #print(i)  print za red fifo
    dodajIispisi(i+1)
    print(i)  #print za stek lifo
dodajIispisi(0)'''

#primer 34 lambda izraz
'''def myfunc(n):
    return lambda a: a*n
my = myfunc(2)
print(my(2)) '''

l = ["jabuka","kruska","sljiva","kajsija"]
for k,v in enumerate(l):
    print(k,v)