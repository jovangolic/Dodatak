graph = {"amin":{"wasim","nick","mike"},"wasim":{"imran","amin"},"imran":{"wasim","faruk"},
         "faruk":{"imran"},"mike":{"amin"},"nick":{"amin"}}
'''def bfs(graph,start): #iterativno
    visited = []
    red = [start]
    while red:
        node = red.pop(0)
        if node not in visited:
            visited.append(node)
            susedi = graph[node]
            for sused in susedi:
                red.append(sused)
    return visited
print(bfs(graph,"amin")) '''

'''def dfs(node,visited,graph): #rekurzivno
    if node not in graph:
        print("node not present")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            dfs(i,visited,graph)
v = set()            
dfs("amin",v,graph)'''

'''def dfs2(graph,start,visited=None): #rekurzivno drugi nacin
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for i in graph[start] - visited:
        dfs2(graph,i,visited)
    return visited
v = set()
print(dfs2(graph,"amin",v)) '''

'''def dfs_iter(node,graph): #iterativno
    visited = set()
    if node not in graph:
        print("node not present")
        return
    stack = []
    stack.append(node)
    while stack:
        curr = stack.pop()
        if curr not in visited:
            print(curr)
            visited.add(curr)
            for i in graph[curr]:
                stack.append(i)
#dfs_iter("amin",graph)    
g2 = {"A":{"B","D","C"},"B":{"A","D","E"},"C":{"A","D"},"D":{"A","B","E"},"E":{"B","D"}}
dfs_iter("A",g2) '''           