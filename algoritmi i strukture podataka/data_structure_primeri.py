#single linked list
'''class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class SingleLinkedList:
    def __init__(self):
        self.head = None
    def travers(self):
        if self.head is None:
            print('linked-list is empty')             
            return
        n = self.head
        while n is not None:
            print(n.data,"-->",end=" ")
            n = n.ref
    def add_first(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  
            return
        n = self.head
        while n.ref is not None:
            n = n.ref
        n.ref = new_node  
    def add_before(self,data,x):
        if self.head is None: #ako je lista prazna
            print('linked list is empty')
            return
        if self.head.data == x: #ako lista ima samo jedan element
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head #dodavanje pre
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print('node is not found')
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
    def add_after(self,data,x):
        n = self.head
        while n.ref is not None:
            if x == n.data:
                break
            n = n.ref
        if n.ref is None:
            print('node is not found')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node   
    def delete_first(self):
        if self.head is None:
            print('ll is empty')
        else:
            self.head = self.head.ref       
    def delete_last(self):
        if self.head is None:
            print('ll is empty')
        elif self.head.ref is None:
            self.head = None    
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None  
    def delete_any(self,x):
        if self.head is None:
            print('ll is empty')
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
            print('node is not found')
        else:
            n.ref = n.ref.ref                                                              
ll1 = SingleLinkedList()
ll1.add_first(10)
ll1.add_first(20)
ll1.add_first(40)
ll1.add_first(50)
#ll1.add_before(9,10)
#ll1.add_before(9,40)
#ll1.insert_empty(1)
#ll1.delete_first()
#ll1.delete_last()
ll1.delete_any(10)
ll1.travers()  '''

class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
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
    def add_first(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node           
    def add_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('list is not empty')
    def add_last(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.nref is not None:
            n = n.nref
        n.nref = new_node
        new_node.pref = n  
    def add_after(self,data,x):
        new_node = Node(data)
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
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node 
    def add_before(self,data,x):
        if self.head is None:
            print('list is empty')
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
            return
        n = self.head
        while n.nref is not None:
            if n.nref.data == x:
                break
            n = n.nref
        if n is None:
            print('node not found')
        else:
            new_node = Node(data)
            new_node.nref = n.nref
            new_node.pref = n
            n.nref.pref = new_node 
            n.nref = new_node
dl1 = DLL()
dl1.add_first(1)
dl1.add_first(2)
#dl1.add_empty(2)
dl1.add_last(3)
#dl1.add_after(4,1)
#dl1.add_after(0,3)
dl1.add_before(6,3)
dl1.travers()
dl1.backward_travers()