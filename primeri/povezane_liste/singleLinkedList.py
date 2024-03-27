
class Node:
    def __init__(self,data=None):
        self.data = data
        self.ref = None
class SLL:
    def __init__(self):
        self.head = None
    def traverse(self):
        if self.head is None:
            print("list is empty")
            return
        n = self.head
        while n is not None:
            print(n.data,"-->",end=" ") 
            n = n.ref  
    def add_first(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node                 
    def add_last(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            n = n.ref
        n.ref = new_node 
    def add_before(self,data,x): #data je podatak koji dodajemo, x cvor od koga dodajes
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
    def add_after(self,data,x):
        if self.head is None:
            print("linked list is empty")
            return
        n = self.head
        while n.ref is not None:
            if n.data == x:
                break
            n = n.ref 
        if n is None:
            print("node not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node                   
    def add_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("list not empty")    
    def delete_first(self):
        if self.head is None:
            print("linked list is empty")   
            return     
        self.head = self.head.ref
    def delete_last(self):
        if self.head is None:
            print("linked list is empty")
        elif self.head.ref is None: #ako lista ima samo jedan element
            self.head = None
        else: # ako ima vise od 2, brises zadnji
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None    
    def delete_any(self,x):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.ref is None:
            if self.head.data == x:
                self.head = None
            else:
                print("node not present")
            return        
        if self.head.data == x:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("node not found")
        else:
            n.ref = n.ref.ref


sl = SLL()
sl.add_first(1)
sl.add_last(3)
sl.add_before(2,3)
sl.add_before(0,1)
sl.add_after(5,1)
sl.add_after(9,3)
#sl.add_empty(2)
#sl.delete_first()
#sl.delete_last()
sl.delete_any(5)
sl.traverse()


