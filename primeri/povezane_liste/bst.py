#stablo/tree
class BST:
    def __init__(self,key=None):
        self.key = key
        self.left = None
        self.right = None
    def insert(self,data):
        if self.key == None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = BST(data)
    
    def pre_order(self):
        print(self.key,end=" ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()
    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.key,end=" ")
        if self.right:
            self.right.in_order()
    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.key,end=" ")
    def search(self,data):
        if self.key == data:
            print("node is found")
            return
        if data < self.key:
            if self.left is not None:
                self.left.search(data)
            else:
                print("node not present")
        else:
            if self.right is not None:
                self.right.search(data)
            else:
                print("node not present") 
    def delete_node(self,data,curr):
        if self.key is None:
            print("tree is empty")
            return
        if data < self.key:
            if self.left is not None:
                self.left = self.left.delete_node(data,curr)
            else:
                print("node not present")
        elif data > self.key:
            if self.right is not None:
                self.right = self.right.delete_node(data,curr)
            else:
                print("node not present")
        else:
            if self.left is None: #brisnje leveog cvora
                temp = self.right #temp postaje None
                if data == curr: #kopiranje i provera da li se brise koreni cvor
                    self.key = temp.key
                    self.left = temp.left
                    self.right = temp.right
                    temp = None #brisanje cvora
                    return
                self = None #brisanje              
                return temp
            if self.right is None: #brisanje desnog cvora
                temp = self.left
                if data == curr:
                    self.key = temp.key
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    return
                self = None
                return temp
            node = self.right 
            while node.left: #trazenje najmanjeg cvora u desnom podstablu
                node = node.left
            self.key = node.key #kopiranje cvorova
            self.right = self.right.delete_node(node.key,curr) #trazimo u desnom podstablu
        return self 
    def min_node(self):
        current = self #current = root; zato ide self.
        while current.left:
            current = current.left
        print("min node is: ",current.key)
    def max_node(self):
        current = self
        while current.right:
            current = current.right
        print("max node is: ",current.key)      
    def min_node2(self): #drugi nacin
        root = self.left
        while root.left:
            root = root.left
        print("min node is: ",root.key)
    def max_node2(self): #drugi nacin
        root = self.right
        while root.right:
            root = root.right
        print("max node is: ",root.key)                                  
                                       
bst = BST(10)
lista = [5,3,4,6,12,11,17,8]
#lista = [1,2]
for i in lista:
    bst.insert(i)
#bst.search(17) 
#bst.delete_node(11)
#bst.pre_order()
def count(node):
    if node is None:
        return 0
    return 1+count(node.left)+count(node.right)
#print(count(bst))
if count(bst) > 1:
    bst.delete_node(10,bst.key)
else:
    print("greska") 
bst.pre_order()
print() 
bst.min_node() 
bst.max_node()                                                                                             

