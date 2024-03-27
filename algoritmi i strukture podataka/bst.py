#npr binary search tree
class BST:
    def __init__(self,key):
        self.key = key
        self.leftchild = None
        self.rightchild = None
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data: #za ignorisanje duplikata
            return
        if self.key > data:
            if self.leftchild:
                self.leftchild.insert(data)
            else:
                self.leftchild = BST(data)    #kreiranje cvora ako je prazno
        else:
            if self.rightchild:
                self.rightchild.insert(data)
            else:
                self.rightchild = BST(data)   #kreiranje cvora ako je prazno    
    def search(self,data):
        if self.key == data:
            print('node is found')
            return
        if data < self.key:
            if self.leftchild:
                self.leftchild.search(data)
            else:
                print('node not present')
        else:
            if self.rightchild:
                self.rightchild.search(data)
            else:
                print('node not present')   
    def pre_order(self): #metod za pretragu traversal
        print(self.key, end=" ")
        if self.leftchild:
            self.leftchild.pre_order()
        if self.rightchild:
            self.rightchild.pre_order()  
    def in_order(self):
        if self.leftchild:
            self.leftchild.in_order()
        print(self.key, end=" ")
        if self.rightchild:
            self.rightchild.in_order()    
    def post_order(self):
        if self.leftchild:
            self.leftchild.post_order()
        if self.rightchild:
            self.rightchild.post_order()
        print(self.key, end=" ")  
    def delete_node(self,data,curr):
        if self.key is None:
            print('tree is empty')
            return
        if data < self.key:
            if self.leftchild:
                self.leftchild = self.leftchild.delete_node(data,curr)
            else:
                print('node not present')
        elif data > self.key:
            if self.rightchild:
                self.rightchild = self.rightchild.delete_node(data,curr)
            else:
                print('node not present')
        else: # za brisanje
            if self.leftchild is None:
                temp = self.rightchild
                if data == curr:
                    self.key = temp.key
                    self.leftchild = temp.leftchild
                    self.rightchild = temp.rightchild
                    temp = None
                    return
                self = None
                return temp
            if self.rightchild is None:
                temp = self.leftchild
                if data == curr:
                    self.key = temp.key
                    self.leftchild = temp.leftchild
                    self.rightchild = temp.rightchild
                    temp = None
                    return
                self = None
                return temp
            node = self.rightchild
            while node.leftchild:
                node = node.leftchild  
            self.key = node.key
            self.rightchild = self.rightchild.delete_node(node.key,curr)    
        return self  
    def min_node(self): #trazenje min imalnog cvora
        current = self  #kreces od korenog cvora, zato ide self
        while current.leftchild:
            current = current.leftchild 
        print('min node is: ',current.key)   
    def max_node(self): #trazenje mx imalnog cvora
        current = self  #kreces od korenog cvora, zato ide self
        while current.rightchild:
            current = current.rightchild
        print('min node is: ',current.key)      
def count(node):
    if node is None:
        return 0
    return 1+count(node.leftchild) + count(node.rightchild)     #0va jedinica je root/koreni cvor                                                                                                    
'''root = BST(10)
l = [6,3,1,6,98,3,7,100]
for i in l:
    root.insert(i)
print('preorder')
root.pre_order()
print()'''
'''if count(root)>1:
    root.delete_node(10,root.key)
else:
    print("can't perform del operation")    
root.pre_order()'''
#root.min_node()
#root.max_node()


'''#npr iterativno racunanje stepena
def stepen(x,n): #x je broj, n ide od 0 do n-1
    y = 1
    for i in range(n):
        y = y * x
        i+=1
    return y
print(stepen(2,3))  
#npr rekurzivno racunanje stepena
def rek_stepen(x,n):
    if n == 0:
        return 1
    return x * rek_stepen(x,n-1) 
print(rek_stepen(2,3)) '''




