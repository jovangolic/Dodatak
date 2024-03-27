
class Node:
    def __init__(self,data=None):
        self.data = data
        self.nref = None
        self.pref = None
class DLL:
    def __init__(self):
        self.head = None
    def forward_traverse(self):
        if self.head is None:
            print("double linked list is empty")
            return
        n = self.head
        while n is not None:
            print(n.data,"->",end="")
            n = n.nref
    def backward_traverse(self):
        print()
        if self.head is None:
            print("double linked list is empty")
            return
        n = self.head
        while n.nref != None:
            n = n.nref
        while n != None:
            print(n.data,"<-",end="")                        
            n = n.pref
    def add_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        print("list not empty")
    def add_first(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.nref = self.head
        self.head.pref = new_node
        self.head = new_node
    def add_last(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.nref is not None:
            n = n.nref
        new_node.pref = n
        n.nref = new_node          
    def add_before(self,data,x):
        if self.head is None:
            print("double linked list is empty")
            return
        n = self.head
        while n.nref is not None:
            if n.data == x:
                break
            n = n.nref
        if n is None:
            print("node not found") 
        else:
            new_node = Node(data)
            new_node.nref = n
            new_node.pref = n.pref
            if n.pref is not None:
                n.pref.nref = new_node
            else:
                self.head = new_node    
            n.pref = new_node   
    def add_before2(self,data,x):
        if self.head is None:
            print("double linked list is empty") 
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
        if n.nref is None:
            print("node note found")
        else:
            new_node = Node(data)
            new_node.nref = n.nref
            new_node.pref = n
            n.nref.pref = new_node
            n.nref = new_node                   
    def add_after(self,data,x):
        if self.head is None:
            print("double linked list is empty")
            return
        n = self.head
        while n.nref is not None:
            if n.data == x:
                break
            n = n.nref
        if n is None:
            print("node not found")
        else:
            new_node = Node(data)
            new_node.nref = n.nref
            new_node.pref = n
            if n.nref is not None:
                n.nref.pref = new_node
            n.nref = new_node 
    def add_after2(self,data,x):
        n = self.head
        while n.nref is not None:
            if n.data == x:
                break
            n = n.nref
        if n is None:
            print("node not found")
        elif n.nref is None:
            new_node = Node(data)
            new_node.pref = n
            n.nref = new_node
        else:
            new_node = Node(data)
            new_node.nref = n.nref
            new_node.pref = n
            n.nref.pref = new_node
            n.nref = new_node   
    def delete_first(self):
        if self.head is None:
            print("double linked list is empty") 
            return
        if self.head.nref is None:
            self.head = None
            return
        self.head = self.head.nref
        self.head.pref = None  
    def delete_last(self):
        if self.head is None:
            print("double linked list is empty") 
            return
        if self.head.nref is None:
            self.head = None
            return
        n = self.head
        while n.nref != None:
            n = n.nref
        n.pref.nref = None  
    def delete_any(self,x):
        if self.head is None:
            print("double linked list is empty") 
            return
        if self.head.nref is None:
            if self.head.data == x:
                self.head = None
            else:
                print("list is empty")
            return
        if self.head.data == x:
            self.head = self.head.nref
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
            if n.data == x:
                n.pref.nref = None
            else:
                print("node not found")      


dl1 = DLL()
#dl1.add_empty(4)
dl1.add_first(2)
dl1.add_first(3)
dl1.add_last(1)
dl1.add_last(5)
dl1.add_before(0,3)
dl1.add_before(4,3)
dl1.add_before(8,1)
dl1.add_before(7,3)
dl1.add_before2(9,0)
dl1.add_before2(6,1)
dl1.add_after(10,4)
dl1.add_after(12,5)
dl1.add_after2(11,12)
dl1.add_after2(19,7)
dl1.add_after2(18,8)
#dl1.delete_first()
#dl1.delete_last()
dl1.delete_any(9)
dl1.delete_any(11)
dl1.delete_any(3)
dl1.delete_any(90)
dl1.forward_traverse()     
dl1.backward_traverse()              
