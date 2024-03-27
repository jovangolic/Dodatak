#binary search

def binary_search(lista,num): #iterativno
    if len(lista) < 1:
        return lista
    found = False
    low = 0
    high = len(lista)-1
    while low <= high and not found:
        mid = (low + high) // 2
        if num == lista[mid]:
            found = True
        elif num > lista[mid]:
            low = mid + 1
        else:
            high = mid - 1    
    if found == True:
        print("num is found")
    else:
        print("num is not found")            
    #return lista            
l = [23,10,18,1,4,3,6]
def sortiranje(lista): #asc
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                lista[i],lista[j] = lista[j],lista[i]
    return lista
#print(sortiranje(l))            
lst = sortiranje(l)
#l.sort()
#binary_search(lst,3)
def search(lista,key): #rekurzivno
    def binary_search_rec(left,right):
        if left <= right:
            mid = (left+right) // 2
            if lista[mid] == key:
                return lista[mid]
            if lista[mid] > key:
                return binary_search_rec(left,mid-1)
            else:
                return binary_search_rec(mid+1,right)
        return False
    return binary_search_rec(0,len(lista)-1)
#print(search(lst,23))

#linearna pretraga
def linear_search(lista,key):
    if len(lista) <= 1:
        return lista
    nova_lista = []
    found = False
    for i in range(len(lista)-1):
        if lista[i] == key:
            nova_lista.append(i)
            found = True
    if found:
        print("key is found")
        for i in nova_lista:
            print(i)
    else:
        print("key not found")            
l = [34,1,5,6,7,1,23,8]
#linear_search(l,23)

l1 = [2,4,1,5,6]
s = ""
for i in l1:
    s+=str(i)
#print(s)
#print(type(s))    
s1 = "".join(str(i) for i in l1)
#print(s1)
#print(type(s1))
lst = ["a","b","v"]
s2 = ""
for i in lst:
    s2 += str(i)
#print(s2)    
#print(type(s2))
s3 = "".join(lst)
print(s3)
print(type(s3))