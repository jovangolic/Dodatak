#graph koristeci adjacency matrix representation
#graph
'''node_count = 0
#nodes = ["a","b","c","d","e"]
#graph = {"A":[0,1,1,1,0],"B":[1,0,0,1,1],"C":[1,0,0,1,0],"D":[1,1,1,0,1],"E":[0,1,0,1,0]}
nodes = []
graph = []
node_count = 0
def add_node(v):
    global node_count
    if v in nodes:
        print(v," is present")
    else:
        nodes.append(v)
        node_count += 1
        for i in graph:
            i.append(0) 
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1," not present")
    elif v2 not in nodes:
        print(v2," not present")
    else:
        idx1 = nodes.index(v1)
        idx2 = nodes.index(v2)
        graph[idx1][idx2] = 1
        graph[idx2][idx2] = 1
def delete_node(v):
    global node_count
    if v not in nodes:
        print_graph(v," not present")
    else:
        idx1 = nodes.index(v)
        node_count -= 1
        nodes.pop(idx1)
        graph.pop(idx1)
        for i in graph:
            i.pop(idx1)
def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1," not present")
    elif v2 not in nodes:
        print(v2," not present")
    else:
        idx1 = nodes.index(v1)
        idx2 = nodes.index(v2)
        graph[idx1][idx2] = 0
        graph[idx2][idx1] = 0        
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"),end=" ")
        print()                                       
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A","B")  
add_edge("A","D")  
add_edge("A","C")  
add_edge("C","D")  
add_edge("B","E")  
add_edge("E","D") 
#delete_node("C")  
delete_edge("A","B")
print(graph)
print_graph()'''


#graph koristeci adjacency list representation
nodes = []
graph = {}
def add_node(v):
    if v in graph:
        print(v," is present")
    else:
        graph[v] = []
def add_edge(v1,v2):
    if v1 not in graph:
        print(v1," not present")
    elif v2 not in graph:
        print(v2," not present")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)   
def add_edge_weighted(v1,v2,cost):
    if v1 not in graph:
        print(v1," not preesnt")
    elif v2 not in graph:
        print(v2," not preent")
    else:
        lista1 = [v2,cost]
        lista2 = [v1,cost]
        graph[v1].append(lista1)
        graph[v2].append(lista2)    
def add_edge_weighted_dir(v1,v2,cost):
    if v1 not in graph:
        print(v1," not present")
    elif v2 not in graph:
        print(v2," not present")
    else:
        lista1 = [v2,cost]
        #lista2 = [v1,cost]
        graph[v1].append(lista1)
        #graph[v2].append(lista2) 
def delete_node(v):
    if v not in graph:
        print(v," not present")
    else:
        graph.pop(v)
        for i in graph:
            lista = graph[i]
            for j in lista:
                if v == j[0]:
                    lista.remove(j)
                    break
        #if v in lista:
        #    lista.remove(v)  
def delete_edge(v1,v2):
    if v1 not in graph:
        print(v1," not present")
    elif v2 not in graph:
        print(v2," not present")
    else:
        #if v2 in graph[v1]:
        #    graph[v1].remove(v2)
        #    graph[v2].remove(v1)
        if v1 in graph[v2]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)    
def delete_edge_undir_weight(v1,v2,cost):
    if v1 not in graph:
        print(v1," not present") 
    elif v2 not in graph:
        print(v2," not present")
    else:
        list1 = [v1,cost]
        list2 = [v2,cost]
        if list2 in graph[v1]:
            graph[v1].remove(list2)
            graph[v2].remove(list1)
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
#add_edge_weighted_dir("A","B",3)
#add_edge_weighted_dir("D","A",2)
#add_edge_weighted_dir("A","C",1)
#add_edge_weighted_dir("B","E",3)
#add_edge_weighted_dir("B","D",5)
#add_edge_weighted_dir("C","D",4)
#add_edge_weighted_dir("E","D",2)
add_edge_weighted("A","B",3)
add_edge_weighted("D","A",2)
add_edge_weighted("A","C",1)
add_edge_weighted("B","E",3)
add_edge_weighted("B","D",5)
add_edge_weighted("C","D",4)
add_edge_weighted("E","D",2)
#delete_node("A")
#add_edge("A","B")
#add_edge("A","D")
#add_edge("A","C")
#add_edge("B","D")
#add_edge("C","D")
#add_edge("B","E")
#add_edge("E","D")
#delete_edge("A","B")
delete_edge_undir_weight("A","B",3)
print(graph) 
