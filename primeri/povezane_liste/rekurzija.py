#rekurzija i bektreking
def factorijel(n):
    if n==0:
        return 1
    f = n*factorijel(n-1)
    print(f,end=",")
    return f
#print(factorijel(5))

l = [4,23,7,6,9,1,0]
def prolazak(index):
    #if index < len(l):
    #    print(l[index],end=" ")
    #    prolazak(index+1)
    if index == len(l):
        return 
    print(l[index],end=" ")
    prolazak(index+1)
#prolazak(0)        
lst = []
def stek(index):
    n = len(l)
    if index == n:
        return 
    lst.append(index)
    stek(index+1)
    print(index,end=",")
#stek(0)
def red(index):
    n = len(l)
    if index == n:
        return 
    lst.append(index)
    print(index,end=",")
    red(index+1)
#red(0)        

def fibonaci(num,lista=[]):
    if num == 0:
        return lista
    if len(lista) < 2:
        lista.append(1)
        fibonaci(num-1,lista)
    else:
        last = lista[-1]
        second_last = lista[-2]
        lista.append(last+second_last)
        fibonaci(num-1,lista)    
    return lista
#print(fibonaci(20))

'''num = int(input("unesi broj: "))
memorija = []
for i in range(num+1):
    memorija.append(0)
def fib_memorija(n):
    if memorija[n] != 0:
        return memorija[n]
    if n == 0 or n == 1:
        return 1
    memorija[n] = fib_memorija(n-1) + fib_memorija(n-2)
    return memorija[n]
print(fib_memorija(num))  '''

def fib(n): #iterativno
    a,b = 0,1
    zbir = 0
    for i in range(1,n+1):
        zbir = a + b
        a = b
        b = zbir
    return zbir
#print(fib(50))    

#print([a+b for a in range(3) for b in range(3)])
#print([a+b for a in "abc" for b in "abc"])

#backtracking
def bitStr(n,s): #s je string, n je njegova duzina
    if n == 1:
        return s
    return [digit + bits for digit in bitStr(1,s) for bits in bitStr(n-1,s)]
#print(bitStr(3,"abc"))

#npr merge sort rekurzivno
def mergeSort(A):
#base case if the input array is one or zero just return.
    if len(A) > 1:
# splitting input array
        print('splitting ', A )
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]
        #recursive calls to mergeSort for left and right sub arrays
        mergeSort(left)
        mergeSort(right)
#initalizes pointers for left (i) right (j) and output array (k)
# 3 initalization operations
        i = j = k = 0
#Traverse and merges the sorted arrays
        while i <len(left) and j<len(right):
# if left < right comparison operation
            if left[i] < right[j]:
# if left < right Assignment operation
                A[k]=left[i]
                i=i+1
            else:
#if right <= left assignment
                A[k]= right[j]
                j=j+1
            k=k+1
        while i<len(left):
#Assignment operation
            A[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
#Assignment operation
            A[k]=right[j]
            j=j+1
            k=k+1
    print('merging ', A)
    return(A)
#print(mergeSort([7,9,3,1,2,5,4,6,0,8]))


#grid paths n x m
def grid_paths(n,m):
    if n == 1 or m == 1:
        return 1
    return grid_paths(n,m-1) + grid_paths(n-1,m)
#print(grid_paths(4,5))

#npr rekurzivna funkciaj koja racuna broj podela za n = k i m = k
def count_partitions(n,m):
    if n == 0:
        return 1
    elif m == 0 or n < 0:
        return 0
    else:
        return count_partitions(n-m,m) + count_partitions(n,m-1)
#print(count_partitions(9,4))   

#npr rekurzivno konvertovanje iz celog broja u binarni
def convert_binary(n):
    if n > 1:
        convert_binary(n //2)
    print(n%2,end=" ") 
#convert_binary(223)       