#npr za graf dodavanje cvora u graf koristeci adjacency matrix representation
'''def add_node(v):
    global node_count
    if v in nodes:
        print('node is present')
    else:
        node_count +=1
        nodes.append(v) 
        for n in graph: #dodati novu kolonu u graf
            n.append(0) 
        temp = [] #novi red
        for i in range(node_count):
            temp.append(0)  
        graph.append(temp)  
#dodavanje grana u graf koristeci adjacency matrix representation
def add_edge(v1,v2): #undirected, unweighted graph
    if v1 not in nodes:
        print(v1,'is not presented')
    elif v2 not in nodes:
        print(v2,'is not present')
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)     
        graph[index1][index2] = 1
        graph[index2][index1] = 1   
def add_edge_weigh(v1,v2,cost): #undirected,weighted graph
    if v1 not in nodes:
        print(v1,'is not presented')
    elif v2 not in nodes:
        print(v2,'is not present')
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)     
        graph[index1][index2] = cost
        graph[index2][index1] = cost  
#brisanje cvora u grafu koristeci adjacency matrix representation
def delete_node(v):
    global node_count
    if v not in nodes:
        print(v,'not present')
    else:
        idx1 = nodes.index(v) #trazenje indeksa
        node_count -= 1
        nodes.remove(v) #brise se iz liste
        graph.pop(idx1) #brise se iz matrice red
        for i in graph: # brisanje kolone
            i.pop(idx1)  
#brisanje grane iz grafa koristeci matrix adjacency repr            
def delete_edge(v1,v2): #undirected,weighted, unweighted
    if v1 not in nodes:
        print(v1,'is not present')
    elif v2 not in nodes:
        print(v2,'is not present')
    else:
        idx1 = nodes.index(v1)
        idx2 = nodes.index(v2)
        graph[idx1][idx2] = 0
        graph[idx2][idx1] = 0        
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"),end=" ")
        print() # za novu liniju                  
nodes = [] #za listu
graph = []  #za matricu
node_count = 0 #koliko ima cvorova
print('before adding nodes')
print(nodes)
print(graph)
add_node('A')
add_node('B')
add_node('D')
add_edge('A','B')
add_edge('A','D')
add_edge_weigh('A','B',10)
add_edge_weigh('A','D',5)
delete_edge('A','C')
print('after adding nodes')
print(nodes)
print(graph)
print_graph()'''

#npr dodavanje cvora i grana koristeci adjacency list representation
def add_node(v): #v = new_node, za directed, undirected
    if v in graph:
        print(v,'is present in graph')
    else:
        graph[v] = []   
def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,'is not present')
    elif v2 not in graph:
        print(v2,'is not present')
    else:
        graph[v1].append(v2)     
        graph[v2].append(v1)  
def add_edge_weight(v1,v2,cost): #undirected, weighted
    if v1 not in graph:
        print(v1,'is not present')
    elif v2 not in graph:
        print(v2,'is not present')  
    else:
        list1 = [v2,cost]
        list2 = [v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)    
def add_edge_dir_weight(v1,v2,cost): #directed, weighted
    if v1 not in graph:
        print(v1,'is not present')
    elif v2 not in graph:
        print(v2,'is not present')
    else:
        list1 = [v2,cost]
        #list2 = [v1,cost]
        graph[v1].append(list1)  
        #graph[v2].append(list2)  
#brisanje cvora u grafu koristeci adjacency list repr  
def delete_node(v): #directed,unweighted, undirected,weighted
    if v not in graph:
        print(v,'is not present')
    else:
        graph.pop(v) #brisanje kljuca
        for i in graph:
            list1 = graph[i]
            #for j in list1: #weighted & undirected
            #    if v == j[0]:
            #        list1.remove(j)
            #        break
            if v in list1:
                list1.remove(v) 
#brisanje grane u grafu koristeci adjacency list repr
def delete_edge(v1,v2): #unweighted undirected
    if v1 not in graph:
        print(v1,'is not present')
    elif v2 not in graph:
        print(v2,'is not present')
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)   
def delete_edge_weight_undir(v1,v2,cost):#weighted, undirected
    if v1 not in graph:
        print(v1,'is not present')
    elif v2 not in graph:
        print(v2,'is not present')
    else:
        temp = [v1,cost]
        temp1 = [v2,cost]
        if temp1 in graph[v1]:
            graph[v1].remove(temp1)
            graph[v2].remove(temp)      
def dfs_rec(node,visited,graph):
    if node not in graph:
        print('node not present')
        return
    if node not in visited:
        print(node)
        visited.add(node)    
        for i in graph[node]:
            dfs_rec(i,visited,graph)
def dfs_iterative(node,graph):
    visited = set()
    if node not in graph:
        print('node not present')
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop() #posto vraca izbaceni element, zato ide promenljiva current
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]: #to je za npr 'a':['b','c','d']
                stack.append(i)
#visited = set()                                                                
graph = {}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
#add_edge_weight('A','B',10)
#add_edge_weight('A','C',5)
print(graph)
#dfs_rec('A',visited,graph)
dfs_iterative('A',graph)


 




