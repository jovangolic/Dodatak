graph = {"amin":{"wasim","nick","mike"},"wasim":{"imran","amin"},"imran":{"wasim","faruk"},
         "faruk":{"imran"},"mike":{"amin"},"nick":{"amin"}}

'''def bfs(graph,start): #iterativno
    visited = [] #na pocetku je lista posecenih cvorova prazna
    queue = [start] #lista cvorova od koga krecem
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited                     
print(bfs(graph,"nick"))    
g2 = {"A":{"B","D","C"},"B":{"A","D","E"},"C":{"A","D"},"D":{"A","B","E"},"E":{"B","D"}}
print(bfs(g2,"A"))     '''

'''def dfs(node,visited,graph): #rekurzivno
    if node not in graph:
        print("node not present")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            dfs(i,visited,graph)
            
visited = set()
g2 = {"A":{"B","D","C"},"B":{"A","D","E"},"C":{"A","D"},"D":{"A","B","E"},"E":{"B","D"}}
dfs("A",visited,g2)'''

'''def dfs2(graph,start,visited=None): #rekurizvno
    if visited is None:
        visited = set()
    visited.add(start)
    print(visited)
    for i in graph[start] - visited:
        dfs2(graph,i,visited)
    return visited       
visit = set() 
print(dfs2(graph,"amin",visit))'''


def dfs_iter(node,graph): #dfs iterativno
    visited = set()
    if node not in graph:
        print("node not present")
        return
    stack = [] # idu vrednosti kljuceva cvora npr amin {w,n,m}
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)
#dfs_iter("amin",graph)  
#g2 = {"A":{"B","D","C"},"B":{"A","D","E"},"C":{"A","D"},"D":{"A","B","E"},"E":{"B","D"}}
#dfs_iter("A",g2)

'''def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]
        merge_sort(left)
        merge_sort(right)
        i,j,k =0,0,0 
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i+=1;k+=1
            else:
                lista[k] = right[j]
                j+=1;k+=1
        while i < len(left):
            lista[k] = left[i]
            i+=1;k+=1
        while j < len(right):
            lista[k] = right[j]
            j+=1;k+=1
    return lista        
l = [3,2,5,1,9,2,4,7,0,1,10]
#print(merge_sort(l))
#print(l)  
def merge(left,right):
    rezultat = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            rezultat.append(left[i])
            i+=1
        else:
            rezultat.append(right[j])
            j+=1
    rezultat += left[i:]
    rezultat += right[j:]
    return rezultat
def mergesort(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    left = mergesort(lista[:mid])
    right = mergesort(lista[mid:])
    return merge(left,right)
print(mergesort(l))             '''

#shell_sort
'''def shell_sort(lista):
    gap = len(lista) // 2
    while gap > 0:
        for i in range(gap,len(lista)):
            curr_elem = lista[i]
            pos = i
            while pos >= gap and curr_elem < lista[pos-gap]:
                lista[pos] = lista[pos-gap]
                pos = pos-gap
            lista[pos] = curr_elem
        gap = gap // 2    
    return lista                                            
l = [3,2,5,1,9,2,4,7,0,1,10]
print(shell_sort(l))'''

def binary_search_iter(lista,key):
    low,high = 0,len(lista)-1
    found = False
    while low <= high and not found:
        mid = (low+high) // 2
        if key == lista[mid]:
            found = True
        elif key > lista[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if found == True:
        print("key found")
    else:
        print("key not found")                                                                   
l = [2,4,5,6,7,1,3,8,10,12,19,2,0,5,13]
#l.sort()
#binary_search_iter(l,9)
def b_search_rec(lista,key):
    def recursion(left,right):
        if left <= right:
            mid = (left+right) // 2
            if key == lista[mid]:
                return True
                #return lista[mid]
            if key > lista[mid]:
                return recursion(mid+1,right)
            else:
                return recursion(left,mid-1)
        return False    
    return recursion(0,len(lista)-1)
#print(b_search_rec(l,9))        
def linear_search(lista,key):
    if len(lista) <= 1:
        return lista
    l = []
    found = False
    for i in range(len(lista)-1):
        if lista[i] == key:
            found = True
            l.append(i)
    if found:
        print("key found")
        for i in l:
            print("pozicija je: ",i)
    else:
        print("key not found")
#linear_search(l,12)  
#print(l)                      

def stepen(base,exponent):
    if exponent < 1:
        return 1
    return base * stepen(base,exponent - 1)
#print(stepen(2,50))                  
def stepen_iter(base,exponent):
    total = 1
    for i in range(1,exponent+1):
        total = total * base
    return total
#print(stepen_iter(2,50))    

#zbir prvih n brojeva rekurzivno i iterativno
def zbir_iter(n):
    total = 0
    for i in range(n+1):
        total += i
    return total
#print(zbir_iter(10))    
def zbir_rec(n):
    if n == 0:
        return 0
    return n+zbir_rec(n-1)
#print(zbir_rec(10))

def fact_rec(n):
    if n == 1 or n == 0:
        return 1
    return n*fact_rec(n-1)
#print(fact_rec(10))
def fact_iter(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    return total
#print(fact_iter(10))

#npr prolazak kroz niz rekurzivno
niz = [9,7,3,5]
def prolaz_rec(index): #index od koga kreces
    if index < len(niz):
        print(niz[index],end=" ")
        prolaz_rec(index+1)
#prolaz_rec(0)        
def prolaz_rec2(index):
    if index == len(niz):
        return 
    print(niz[index],end=" ")
    prolaz_rec2(index + 1)
#prolaz_rec2(0)    

#pravljenje stek i reda rekurzivno
n = 5
niz = []
def napravi_stek(index): #prosledjujes index
    if index == n:
        return
    niz.append(index)
    napravi_stek(index+1)
    print(index,end=" ")
#napravi_stek(0)
#print()    
def napravi_red(index):
    if index == n:
        return
    niz.append(index)
    print(index,end=" ")
    napravi_red(index+1)
#napravi_red(0)  
def napravi(index):
    if index == n:
        return
    niz.append(index)
    print(index,end=" ")
    napravi(index+1)
    print(index,end=" ")
#napravi(0)    

#fibonaci iterativno dinamicko programiranje
#num = int(input("unesi broj: "))   
def fib_iter(n):
    suma=0
    a=0;b=1
    if n == 0 or n < 0:
        return 1
    for i in range(1,n+1):
        a=b
        b=suma
        suma=a+b
    return suma    
#print(fib_iter(num))        

#fibonaci rekurzivno
#num = int(input("unesi broj: "))
def fib_rec(n):
    if n == 0 or n == 1:
        return 1
    return fib_rec(n-1)+fib_rec(n-2)
#print(fib_rec(num))
   
#igrica iks oks ceo kod
'''print('dobrodosli u iks,oks igru')
kraj=True
polja = [['P','P','P'],['P','P','P'],['P','P','P']]
def tabla(polje):
    for i in range(len(polje)):
        for j in range(len(polje)):
            print(polje[i][j],end=" ")
        print()
    
def is_kraj():
    for i in range(len(polja)):
        for j in range(len(polja)):
            if ((polja[0][0]=='X') and (polja[0][1]=='X')and (polja[0][2]=='X')
            or (polja[1][0]=='X') and (polja[1][1]=='X')and (polja[1][2]=='X')
            or (polja[2][0]=='X')and (polja[2][1]=='X')and (polja[2][2]=='X')
            or (polja[0][0]=='X')and (polja[1][0]=='X')and (polja[2][0]=='X')
            or (polja[0][1]=='X') and(polja[1][1]=='X') and (polja[2][1]=='X')
            or (polja[0][2]=='X') and (polja[1][2]=='X') and (polja[2][2]=='X')
            or ((polja[i][j]=='X') and i==j) or ((polja[i][j]=='X') and (i+j)==(2))):
                print('igrac 1(x) je pobedio.')
                return False
            elif ((polja[0][0]=='Y') and (polja[0][1]=='Y')and (polja[0][2]=='Y')
            or (polja[1][0]=='Y') and (polja[1][1]=='Y')and (polja[1][2]=='Y')
            or (polja[2][0]=='Y')and (polja[2][1]=='Y')and (polja[2][2]=='Y')
            or (polja[0][0]=='Y')and (polja[1][0]=='Y')and (polja[2][0]=='Y')
            or (polja[0][1]=='Y') and(polja[1][1]=='Y') and (polja[2][1]=='Y')
            or (polja[0][2]=='Y') and (polja[1][2]=='Y') and (polja[2][2]=='Y')
            or ((polja[i][j]=='Y') and i==j) or ((polja[i][j]=='Y') and (i+j)==(2))):
                print('igrac 2(y) je pobedio.')
                return False
            else:
                return True

def igrac1():
    red=int(input('unesi X=x: '))
    kolona = int(input('unesi X=y:'))
    polja[red][kolona]='X '
    tabla(polja)
    is_kraj()
def igrac2():
    red = int(input('unesi X=x: '))
    kolona = int(input('unesi X=y: '))
    polja[red][kolona] = 'Y '
    tabla(polja)
    is_kraj()
while kraj:
    igrac1()
    igrac2() '''    

#npr deo saha, skakac figura
'''start = [int(input("x: ")),int(input("y: "))] 
available = [
    [start[0]-1,start[1]-2],
    [start[0]-2,start[1]-1],
    [start[0]+1,start[1]-2],
    [start[0]+2,start[1]-1],
    [start[0]-1,start[1]+2],
    [start[0]-2,start[1]+1],
    [start[0]+1,start[1]+2],
    [start[0]+2,start[1]+1]
] 
used_positions = 0
letters = ['A','B','C','D','E','F','G','H']
for y in range(8):
    print(y+1,end=" ")
    for x in range(8):
        chr = "O"
        if [x+1,y+1] == start:
            chr = "S"
        if [x+1,y+1] in available:
            used_positions+=1
            chr = "M"
        print(chr,end="")
    print()
print(end="  ")
for l in letters:
    print(l,end="")
print()
print("Possible positions:",used_positions)'''

#npr iz decimalnog u binarni rekurzivno
'''def convert_binanry_rec(n):
    if n > 1:
        convert_binanry_rec(n // 2)
    print(n % 2,end=" ")
convert_binanry_rec(223) '''       

#npr binarna pretraga rekurzivno
'''l1 = [10,1,0,20,-1,7,9,4,3]
def binary_search_rec3(lista,left,right,x):
    if left > right:
        return -1
    mid = (left+right)//2
    if x == lista[mid]:
        return lista[mid]
    if x > lista[mid]:
        return binary_search_rec3(lista,mid+1,right,x)
    else:
        return binary_search_rec3(lista,left,mid-1,x)      
l1.sort()
print(binary_search_rec3(l1,0,len(l1)-1,91))  '''      

def fibonaci(n,lista=[]):
    if n == 0:
        return lista
    if len(lista) < 2:
        lista.append(1)
        fibonaci(n-1,lista)
    else:
        last = lista[-1]
        second_last = lista[-2]
        lista.append(last+second_last)
        fibonaci(n-1,lista)
    return lista
#print(fibonaci(10))        