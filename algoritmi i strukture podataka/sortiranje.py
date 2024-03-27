#selection sort
#npr selection sort bez duplikata ascending
'''list1 = [56,3,2,78,6,0]
print(list1)
for i in range(len(list1)):
    min_val = min(list1[i:])
    min_ind = list1.index(min_val)
    list1[i],list1[min_ind] = list1[min_ind],list1[i]
print(list1)'''

#npr za descending selection sort bez duplikata
'''list1 = [56,3,2,78,6,0]
print(list1)
for i in range(len(list1)):
    min_val = max(list1[i:])
    min_ind = list1.index(min_val)
    list1[i],list1[min_ind] = list1[min_ind],list1[i]
print(list1)'''

#za duplikate
'''l3 = [56,0,2,2,6,0]
print(l3)
for i in range(len(l3)-1):
    min_val = min(l3[i:])
    min_ind = l3.index(min_val,i)
    if l3[i] != l3[min_ind]:
        l3[i],l3[min_ind] = l3[min_ind],l3[i]
print(l3)'''

'''l4 = [34,5,6,81,0,5]
print(l4)
for i in range(len(l4)-1):
    m_ind = i #indeks
    for j in range(i+1,len(l4)):
        if l4[j] < l4[m_ind]: #za ascending, a za descending samo promeni znak u ovo >
            m_ind = j
    if l4[i] != l4[m_ind]:
        l4[i],l4[m_ind] = l4[m_ind],l4[i]
print(l4) '''

#sa korisnickim unosom
'''num = int(input('koliko brojeva unosis: '))
l1 = [int(input('enter number: ')for x in range(num))]
print(l1)
for i in range(len(l1)-1):
    m_ind = i
    for j in range(i+1,len(l1)):
        if l1[j]<l1[m_ind]:
            m_ind = j
    if l1[i] != l1[m_ind]:
        l1[i],l1[m_ind] = l1[m_ind],l1[i]
print(l1)'''


#BUBBLE SORT
'''list1 = [10,15,4,23,0]
print(list1)
for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):
        if list1[i] > list1[i+1]:
            list1[i],list1[i+1] = list1[i+1],list1[i]

print(list1)         
#korisnicki unosi
list1 = []
num = int(input('koliko brojeva unosis: '))
print('enter values: ')
for k in range(num):
    list1.append(int(input()))
for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):
        if list1[i] > list1[i+1]:
            list1[i],list1[i+1] = list1[i+1],list1[i]
print(list1)  '''


#QUICKSORT ako je pivot prvi element
'''def pivot_place(list1,first,last): #funk za trazenje pozicije pivota; first,last su indeksi
    pivot = list1[first]
    left = first+1
    right = last
    while True:
        while left <= right and list1[left] <= pivot:
            left +=1
        while left <= right and list1[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            list1[left],list1[right] = list1[right],list1[left]
    list1[first],list1[right] = list1[right],list1[first] 
    return right
def quicksort(list1,first,last):
    if first < last:
        p = pivot_place(list1,first,last)
        quicksort(list1,first,p-1)
        quicksort(list1,p+1,last)
#main
list1 = [56,26,93,17,31,44]
n= len(list1) 
quicksort(list1,0,n-1)    
print(list1)'''
#random element kao pivot
'''import random 
def pivot_place(list1,first,last):
    rindex = random.randint(first,last)
    list1[rindex],list1[last] = list1[last],list1[rindex]
    pivot = list1[last]
    left = first
    right = last -1
    while True:
        while left <= right and list1[left] >= pivot:
            left +=1
        while left <= right and list1[right] <= pivot:
            right -= 1
        if right < left:
            break
        else:
            list1[left],list1[right] = list1[right],list1[left]
    list1[last],list1[left] = list1[left],list1[last] 
    return left
def quicksort(list1,first,last):
    if first < last:
        p = pivot_place(list1,first,last)
        quicksort(list1,first,p-1)
        quicksort(list1,p+1,last)
list1 = [56,26,93,17,31,44,67]
n= len(list1) 
quicksort(list1,0,n-1)    
print(list1)'''

#median of 3 values
'''import statistics
def pivot_place(list1,first,last):
    low = list1[first]
    high = list1[last]
    mid = (first+last)//2
    pivot_val = statistics.median([low,list1[mid],high])
    if pivot_val == low:
        pindex = first
    elif pivot_val == high:
        pindex = last
    else:
        pindex = mid 
    list1[last],list1[pindex] = list1[pindex],list1[last]
    pivot = list1[last]
    left = first
    right = last -1
    while True:
        while left <= right and list1[left] >= pivot:
            left +=1
        while left <= right and list1[right] <= pivot:
            right -= 1
        if right < left:
            break
        else:
            list1[left],list1[right] = list1[right],list1[left]
    list1[last],list1[left] = list1[left],list1[last] 
    return left
def quicksort(list1,first,last):
    if first < last:
        p = pivot_place(list1,first,last)
        quicksort(list1,first,p-1)
        quicksort(list1,p+1,last)
list1 = [56,26,93,17,31,44,67]
n= len(list1) 
quicksort(list1,0,n-1)    
print(list1)'''


#MERGE SORT
'''def mergesort(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i = 0; j = 0; k= 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i]<right_list[j]:
                list1[k] = left_list[i]
                i+=1; k+=1
            else:
                list1[k] = right_list[j] 
                j+=1; k+=1
        while i < len(left_list):
            list1[k] = left_list[i]
            i+=1; k+=1
        while j < len(right_list):
            list1[k] = right_list[j]
            j+=1; k+=1

num = int(input('koliko elemenata unosis: '))
list1 = [int(input()) for x in range(num)]
mergesort(list1)
print('sorted list is: ',list1)'''

#INSERTION SORT
'''def insertion_sort(list1):
    for index in range(1,len(list1)):
        current_elem = list1[index]
        pos = index
        while current_elem < list1[pos-1] and pos > 0:
            list1[pos] = list1[pos-1]
            pos -= 1
        list1[pos] = current_elem    
list1 = [2,4,3,5,1]
insertion_sort(list1)
print(list1)'''

#npr shell sort
'''def shell_sort(list1):
    gap = len(list1)//2
    while gap > 0:
        for index in range(gap,len(list1)):
            current_elem = list1[index]
            pos = index
            while pos >= gap and current_elem <list1[pos-gap]: #stopping condition
                list1[pos] = list1[pos-gap]
                pos = pos - gap
            list1[pos] = current_elem
        gap = gap//2        
num = int(input('unesi duzinu liste: '))
list1 = [int(input()) for x in range(num)]
shell_sort(list1)
print(list1)'''

#binary search
'''def binary_search(list1,key):
    low = 0 
    high = len(list1)-1
    found = False
    while low <= high and not found:  
        mid = (low+high)//2  
        if key == list1[mid]:
            found = True
        elif key > list1[mid]:
            low = mid+1
        else:
            high = mid-1    
    if found == True:
        print('key is found')
    else:
        print('key not found')                        
list1 = [23,1,4,2,3]
list1.sort()
print(list1)
key = int(input('enter the key: '))
binary_search(list1,key)'''


'''s1 = "The quick brown fox"
for i in range(len(s1)-1,-1,-1):
    print(s1[i],end="")
'''
    
