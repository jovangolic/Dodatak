
class Node:
    def __init__(self,data=None):
        self.data = data
        self.ref = None

            
class CSLL:
    def __init__(self):
        self.head = None
        self.end = None
    def traverse(self):
        if self.head is None:
            print("csll is empty")
            return
        n = self.head
        while n.ref:
            print(n.data,"->",end="")    
            n = n.ref
            if n == self.head:
                break
    def add_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            new_node.ref = self.head
            self.end = new_node
            return
        print("list is not empty")
    def add_first(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            new_node.ref = self.head
            self.end = new_node
            return
        if self.end != None:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            self.end.ref = new_node
    def add_last(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            new_node.ref = self.head
            self.end = new_node
            return
        if self.end != None:
            new_node = Node(data)
            self.end.ref = new_node
            self.end = new_node
            new_node.ref = self.head
    def add_after(self,data,x):
        if self.head is None:
            print("list is empty")
            return
        n = self.head
        while n is not self.end:
            if n.data == x:
                break
            n = n.ref
        if n.data != x:
            print("node not found")
            return
        if n.data == self.end:
            self.add_last(data)
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("list is empty")
            return
        n = self.head
        if n.data == x:
            self.add_first(data)
            return
        while n.ref is not self.end:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref.data != x:
            print("node not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node  
    def delete_first(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head != self.end:
            self.head = self.head.ref
            self.end.ref = self.head
        else:
            self.head=self.end=None   
    def delete_last(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head != self.end:
            n = self.head
            while n.ref.ref is not self.end:
                n = n.ref
            self.end = n
            self.end.ref = self.head
        else:
            self.head=self.end = None    
    def delete_any(self,x):
        if self.head is None:
            print("list is empty")
            return
        if self.head.data == x:
            self.delete_first()
            return
        n = self.head
        while n.ref is not self.end:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref.data != x:
            print("node not found") 
        else:
            n.ref = n.ref.ref       
                                                     

csll = CSLL()
#csll.add_empty(1)
csll.add_first(3)
csll.add_first(2)
csll.add_first(8)
csll.add_last(7)
csll.add_last(9)
csll.add_after(10,9)
csll.add_after(4,3)
csll.add_before(6,8)
csll.add_before(1,3)
#csll.delete_first()
#csll.delete_last()
csll.delete_any(6)
csll.delete_any(9)
csll.delete_any(3)
csll.traverse()
                          