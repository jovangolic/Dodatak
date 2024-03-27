#npr stack koristeci listu
'''stack = []
def push():
    if len(stack) == n:
        print("list is full")
    else:
        element = input("enter the element ")
        stack.append(element)
        print(stack)
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e = stack.pop()
        print("removed element: ",e) 
        print(stack)
n = int(input("limit of stack"))        
while True:
    print("select the operation 1 push, 2 pop, 3 quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("enter the correct operation")  '''
#npr stack koristeci module
# collections module - deque; queue - lifoqueue
'''import collections                     
stack = collections.deque()
stack.append(10)
stack.append(20)
stack.append(30)
#print(stack)
import queue
st = queue.LifoQueue(3)
st.put(10)
st.put(20)
st.put(30)
st.put(40,timeout=1)
print(st)'''

#npr queue
'''queue = []
def enqueue():
    element = input("enter the element: ")
    queue.append(element)
    print(element,"is added to queue")
def dequeue():
    if not queue:
        print("queue is empty") 
    else:
        e = queue.pop(0)
        print("removed element: ",e)   
def display():
    print(queue)
while True:
    print("select the operation 1 add, 2 remove, 3 show, 4 quit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("enter the correct operation")  '''

#npr single linked list
'''class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
    def print_ll(self):
        if self.head is None:
            print("linked list is empty") 
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.ref   
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node   
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node   
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref    
        if n is None:
            print("node is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node   
    def add_before(self,data,x):
        if self.head is None:
            print('list is empty')
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node 
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('list is not empty')    
    def delete_begin(self):
        if self.head is None:
            print("list is empty")
            return
        self.head = self.head.ref   
    def delete_end(self):
        if self.head is None:
            print("list is empty")
        elif self.head.ref is None:
            self.head = None    
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None  
    def delete_by_value(self,x):
        if self.head is None:
            print("list is empty")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("node is not present")
        else:
            n.ref = n.ref.ref                                              
ll1 = LinkedList()
ll1.add_begin(10)
#ll1.delete_begin()
#ll1.add_end(100)
ll1.add_begin(20)
ll1.add_begin(30)
#ll1.add_before(20,10)
#ll1.add_before(30,100)
#ll1.insert_empty(10)
#ll1.delete_end()
ll1.delete_by_value(30)
ll1.print_ll() '''

#npr double linked list
'''class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
class DLinkedList:
    def __init__(self):
        self.head = None
    def print_forward(self):
        if self.head is None:
            print('list is empty')
            return
        n = self.head
        while n is not None:
            print(n.data,"-->",end=" ")
            n = n.nref
    def print_backward(self):
        print()
        if self.head is None:
            print('list is empty')
            return
        n = self.head
        while n.nref is not None:
            n = n.nref
        while n is not None:
            print("<--",n.data,end=" ")
            n = n.pref
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    def add_last(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n 
    def add_after(self,data,x):
        if self.head is None:
            print('list is empty')
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print('node not found')
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node
    def add_before(self,data,x):
        if self.head is None:
            print('list is empty')
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print('node not found')
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node     
    def delete_begin(self):
        if self.head is None:
            print('list is empty')
            return
        if self.head.nref is None:
            self.head = None
        else:
            self.head = self.head.nref
            self.head.pref = None   
    def delete_end(self):
        if self.head is None:
            print('list is empty')
            return
        if self.head.nref is None:
            self.head = None
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None  
    def delete_any(self,x):
        if self.head is None:
            print('list is empty')
            return
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print('node not found')
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print('node not found')                                                                                                                              
dl1 = DLinkedList()
dl1.add_begin(10)
dl1.add_begin(20)
dl1.add_last(30)
dl1.add_after(11,10)
dl1.add_after(12,30)
dl1.add_before(1,20)
dl1.add_before(8,10)
dl1.delete_begin()
dl1.delete_end()
dl1.delete_any(10)
dl1.print_forward()
dl1.print_backward() '''

'''class Node:
    def __init__(self,data):
        self.data = data
        self.pref = None
        self.nref = None
class DLL:
    def __init__(self):
        self.head = None
    def travers(self):
        if self.head is None:
            print('list is empty')
            return
        n = self.head
        while n is not None:
            print(n.data,"-->",end=" ")
            n = n.nref
    def backward_travers(self):
        print()
        if self.head is None:
            print('list is empty')
            return
        n = self.head
        while n.nref is not None:
            n = n.nref
        while n is not None:
            print(n.data,"-->",end=" ")
            n = n.pref
    def add_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('list is not empty')
    def add_first(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        new_node = Node(data)
        new_node.nref = self.head
        self.head.pref = new_node
        self.head = new_node
    def add_last(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        n = self.head
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        new_node.pref = n
        n.nref = new_node  
    def add_after(self,data,x):
        if self.head is None:
            print('list is empty')
            return
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.nref
        if n is None:
            print('node not found')
        else:
            new_node = Node(data)
            new_node.pref = n
            new_node.nref = n.nref
            if n.nref is not None:
                n.nref.pref = new_node
            n.nref = new_node    
    def add_before(self,data,x):
        if self.head is None:
            print('list is empty')
            return
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.nref
        if n is None:
            print('node not found')
        else:
            new_node = Node(data)
            new_node.nref = n
            new_node.pref = n.pref
            if n.pref is not None:
                n.pref.nref = new_node
            else:
                self.head = new_node
            n.pref = new_node   
    def delete_first(self):
        if self.head is None:
            print('list is empty')
            return
        if self.head.nref is None:
            self.head = None
            return
        self.head = self.head.nref
        self.head.pref = None  
    def delete_last(self):
        if self.head is None:
            print('list is empty')
            return
        if self.head.nref is None:
            self.head = None
            return
        n = self.head
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None  
    def delete_any(self,x):
        if self.head is None:
            print('list is empty')
            return
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print('node not present')    
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if n.data == x:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if x == n.data:
                n.pref.nref = None
            else:
                print('node not present')                                                                     
dl1 = DLL() 
#dl1.add_empty(1)
dl1.add_first(2)
dl1.add_first(4)
dl1.add_last(0)
dl1.add_last(8)
dl1.add_after(5,8)
dl1.add_before(3,4)
dl1.add_before(7,0)
dl1.delete_first()
dl1.delete_last()
dl1.delete_any(1)
dl1.travers()
dl1.backward_travers() '''

#npr kruzna lista
'''class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class CLL:
    def __init__(self):
        self.head = None
    def travers(self):
        if self.head is None:
            print('list is empty') 
            return
        n = self.head
        while n is not None:
            print(n.data,"-->",end=" ")
            n = n.ref
            if n == self.head: #izlaz iz kruzne liste, da se ne udje u beskonacnu petlju
                break           
    def add_first(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.ref = new_node
            self.head = new_node
        else:
            n = self.head
            while n.ref != self.head:
                n = n.ref
            new_node = Node(data)
            n.ref = new_node
            new_node.ref = self.head
            self.head = new_node 
    def add_last(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.ref = new_node
            self.head = new_node
        else:
            n = self.head
            while n.ref != self.head:
                n = n.ref
            new_node = Node(data)
            n.ref = new_node
            new_node.ref = self.head  
    def delete_first(self):
        if self.head is None:
            print('list is empty')
            return
        n = self.head
        while n.ref != self.head:
            n = n.ref         
        self.head = self.head.ref
        n.ref = self.head
cl1 = CLL()
cl1.add_first(1)
cl1.add_first(2)
cl1.add_last(8)
cl1.add_last(6)
cl1.delete_first()
cl1.delete_first()
cl1.delete_first()
cl1.delete_first()
cl1.travers()    '''  

#npr circular single linked-list
'''class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class CLL:
    def __init__(self):
        self.head = None
        self.end = None
    def travers(self):
        if self.head == None:
            print('cll is empty')
            return
        n = self.head
        while n.ref:
            print(n.data,"-->",end=" ")
            n = n.ref
            if n == self.head:
                break
    def add_last(self,data):
        new_node = Node(data)
        if self.head == None:
            new_node.ref = new_node
            self.head = new_node
            return 
        n = self.head
        while n.ref != self.head:
            n = n.ref
        n.ref = new_node
        new_node.ref = self.head   
    def add_first(self,data):
        new_node = Node(data)
        if self.head == None:
            new_node.ref = new_node
            self.head = new_node
            return
        n = self.head
        while n.ref is not self.head:
            n = n.ref
        new_node.ref = self.head
        self.head = new_node
        n.ref = new_node
        return 
    def add_after(self,data,x):
        n = self.head
        while n.ref != self.end:
            if n.data == x:
                break
            n = n.ref
        if n.data != x:
            print('node not found') 
            return
        if n.data == self.end:
            self.add_last()
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node   
    def add_before(self,data,x):
        n = self.head
        if n.data == x:
            self.add_first()
            return
        while n.ref != self.end:
            if n.ref.data == x:
                break
            n =n.ref
        if n.ref.data != x:
            print('node not present')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node  
    def delete_first(self):
        n = self.head
        if self.head == None:
            print('list is empty') 
        else:
            if self.head != self.end:
                self.head = self.head.ref
                n.ref = self.head
            else:
                self.head = self.end = None   
    def delete_last(self):
        if self.head == None:
            return
        else:
            if self.head != self.end:
                n = self.head
                while n.ref != self.end:
                    n = n.ref
                self.end = n
                self.end.ref = self.head
            else:
                self.head = self.end = None  
    def delete_any(self,x):
        if self.head is None:
            print('cll is empty')
            return
        if x == self.head.data:
            self.delete_first()
            return
        n = self.head
        while n.ref is not self.end:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref.data != x:
            print('node not present')
        else:
            n.ref = n.ref.ref                                                                                
cl1 = CLL()
cl1.add_first(1)
cl1.add_first(5)
cl1.add_last(4)
cl1.add_last(3)
cl1.add_after(7,1)
cl1.add_after(0,3)
cl1.add_before(9,4)
cl1.delete_first()
#cl1.delete_last()
cl1.delete_any(9)
cl1.delete_any(1)
cl1.travers() '''


                                 

                