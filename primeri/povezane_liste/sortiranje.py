#selection sort
'''l1 = [5,3,2,7,6,0]
def selection_sort_asc(lista): #za ne duplikate
    for i in range(len(lista)):
        min_value = min(lista[i:])
        min_index = lista.index(min_value)
        lista[i],lista[min_index] = lista[min_index],lista[i]
    return lista    
#print(selection_sort_asc(l1))
def selection_sort_desc(lista): #za ne duplikate
    for i in range(len(lista)):
        max_value = max(lista[i:])
        max_index = lista.index(max_value)
        lista[i],lista[max_index] = lista[max_index],lista[i]
    return lista
#print(selection_sort_desc(l1))    
def selection_sort(lista):
    duzina = len(lista)
    for i in range(duzina):
        mini = i
        for j in range(i+1,duzina):         
            if lista[j] < lista[mini]:
                mini_idx = j
        lista[mini],lista[mini_idx] = lista[mini_idx],lista[mini]
    return lista
#print(selection_sort(l1))  
l2 = [5,6,0,2,2,7,0]
def sel_sort_asc(lista): #za duplikate
    for i in range(len(lista)):
        min_val = min(lista[i:])
        min_idx = lista.index(min_val,i)
        lista[i],lista[min_idx] = lista[min_idx],lista[i]
    return lista
#print(sel_sort_asc(l2))

l3 = [34,5,6,8,1,0,5]
def sel_sort(lista): # asc,za duplikate
    n = len(lista)
    for i in range(n-1):
        m_idx = i
        for j in range(i+1,n):
            if lista[j] < lista[m_idx]:
                m_idx = j
        if lista[i] != lista[m_idx]: #za duplikate
            lista[i],lista[m_idx] = lista[m_idx],lista[i]                                 
    return lista
#print(sel_sort(l3))

def selection_sort_input(lista):
    for i in range(len(lista)-1):
        min_val = min(lista[i:])
        min_index = lista.index(min_val,i)
        lista[i],lista[min_index] = lista[min_index],lista[i]
    return lista    
l = [34,5,6,81,0,5]
num = int(input("koliko brojeva unosis: "))
lista2 = [int(input("unesi broj: ")) for i in range(num)]
#print(selection_sort_input(lista2))    '''

#bubble sort
'''l = [10,15,4,23,0,16,11,3]
def bubble_sort(lista): # radi i za duplikate
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]: # > za asc; < za desc
                lista[i],lista[j] = lista[j],lista[i]
    return lista            
#print(bubble_sort(l))        
#num = int(input("koliko brojeva unosis: "))
#lista = [int(input("unesi broj: ")) for _ in range(num)]
#print(bubble_sort(lista))

def bubble_sort2(lista): #radi i za duplikate
    for i in range(len(lista)-1): #prva petlja je samo za iteraciju
        for j in range(len(lista)-1-i): #tu se desava sortiranje
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
    return lista
#num = int(input("koliko brojeva unosis: "))
#lista = [int(input()) for i in range(num)]
#print(bubble_sort2(lista))   '''

#insertion sort
'''l = [2,4,3,1,6,5]
def insertion_sort(lista):
    for i in range(1,len(lista)):
        curr = lista[i]
        pos = i
        while curr < lista[pos-1] and pos > 0:
            lista[pos] = lista[pos-1]
            pos -= 1
        lista[pos] = curr
    return lista
#print(insertion_sort(l))        
def insertion_sort2(lista):
    for i in range(1,len(lista)):
        temp = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > temp:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = temp
    return lista
#print(insertion_sort2(l))        
def insertion_sort3(lista): 
    for index in range(1,len(lista)):
        value = lista[index]
        i = index - 1
        while i >= 0:
            if value > lista[i]:
                lista[i+1] = lista[i]
                lista[i] = value
                i -= 1
            else:break
    return lista            
print(insertion_sort3(l))'''


#quick sort
# ako je pivot na pocetku
'''def pivot_place(lista,firstIdx,lastIdx): #firstIdx,lastIdx su indeksi
    pivot = lista[firstIdx]
    left = firstIdx + 1
    right = lastIdx
    while True:
        while left <= right and lista[left] <= pivot:
            left += 1
        while left <= right and lista[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            lista[left],lista[right] = lista[right],lista[left]
    lista[firstIdx],lista[right] = lista[right],lista[firstIdx]
    return right
def quick_sort(lista,first,last):
    if first < last:
        p = pivot_place(lista,first,last)
        quick_sort(lista,first,p-1)
        quick_sort(lista,p+1,last)            

l = [56,26,93,34,17,31,44]
#quick_sort(l,0,len(l)-1)  
#print(l)    

#random element kao pivot
import random
def find_pivot(lista,start,end):
    r_index = random.randint(start,end) #trazimo slucajni index u listi cija ce vrednost postati pivot
    lista[r_index],lista[end] = lista[end],lista[r_index]
    pivot = lista[end]
    left = start
    right = end -1
    while True:
        while left <= right and lista[left] <= pivot:
            left += 1
        while left <= right and lista[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            lista[left],lista[right] = lista[right],lista[left]
    lista[end],lista[left] = lista[left],lista[end]
    return left                                   
def quick_sort2(lista,first,last):
    if first < last:
        p = find_pivot(lista,first,last)
        quick_sort2(lista,first,p-1)
        quick_sort2(lista,p+1,last)
#quick_sort2(l,0,len(l)-1)
#print(l)                  

#median of 3 value
import statistics
def pivot(lista,first,last):
    low = lista[first]
    high = lista[last]
    mid = (low + high)// 2
    pivot_val = statistics.median([low,lista[mid],high])
    if pivot_val  == low:
        p_index = first
    elif pivot_val == high:
        p_index = last
    else:
        p_index = mid
    lista[last],lista[p_index] = lista[p_index],lista[last]
    pivot = lista[last]
    left = first
    right = last-1
    while True:
        while left <= right and lista[left] >= pivot:
            left += 1
        while left <= right and lista[right] <= pivot:
            right -= 1
        if right < left:
            break
        else:
            lista[left],lista[right] = lista[right],lista[left]
    lista[last],lista[left] = lista[left],lista[last]
    return left
def quick_sort3(lista,first,last):
    if first < last:
        p = pivot(lista,first,last)
        quick_sort3(lista,first,p-1)
        quick_sort3(lista,p+1,last)
n = len(l)        
quick_sort3(l,0,n-1)
print(l)        '''


#merge sort
'''def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]
        merge_sort(left);merge_sort(right)
        i=0;j=0;k=0 # i je za levu stranu, j za desnu stranu; k za novu listu u kojoj idu i-ti i j-ti elementi
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
l = [56,26,93,17,31,33,44,67]
#merge_sort(l)
#print(l)                         
def merge(left,right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result
def mergesort(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    left = mergesort(lista[:mid])
    right = mergesort(lista[mid:])
    return merge(left,right)
print(mergesort(l))'''

#shell sort
def shell_sort(lista):
    gap = len(lista)//2
    while gap > 0:
        for index in range(gap,len(lista)):
            curr_elem = lista[index]
            pos = index
            while pos >= gap and curr_elem < lista[pos-gap]:
                lista[pos] = lista[pos-gap]
                pos -= gap
            lista[pos] = curr_elem
        gap = gap // 2
    return lista            
#l = [56,26,93,17,31,33,44,67]    
#print(shell_sort(l))


#sortiranje string-a
def sort_string(str1):
    slova = list(str1)
    n = len(slova)
    for i in range(n):
        for j in range(0,n-i-1):
            if slova[j] > slova[j+1]:
                slova[j],slova[j+1] = slova[j+1],slova[j]
    return "".join(slova)            

s = "geekforgeeks"
#print(sort_string(s))

#pronalazenje duplikata u listi
a = [1,2,3,2,1,5,6,5,5,5]
seen = set()
dupes = []
for x in a:
    if x in seen:
        dupes.append(x)
    else:
        seen.add(x)                                      
#print(a)
#print(dupes) 
l = []
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if (a[i] == a[j] and (i != j)):
            seen.add(a[i])    
#print(seen)            

       