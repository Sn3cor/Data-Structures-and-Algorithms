from kol2testy import runtests
from collections import deque

def check_connectivity(E,n,s):
    G = [[] for _ in range(n)]
    weight = 0
    for u,v,w in E:
        G[u].append(v)
        G[v].append(u)
        weight += w

    visited = [0 for _ in range(len(G))]
    parent = [None for _ in range(len(G))]
    visited[s] = 1
    queue = deque([s])

    while queue:
        u = queue.popleft()

        for v in G[u]:
            if not visited[v]:
                visited[v] = 1
                parent[v]=u
                queue.append(v)
            elif v != parent[u]: return None

    return None if min(visited) == 0 else weight
    
def beautree(G):
    
    E = []
    for u in range(len(G)):
        for v,w in G[u]:
            if u<v:
                E.append((u,v,w))
    
    E.sort(key = lambda x: x[2])
    i = 0
    j = len(G)-1
    
    while j< len(E):
        weight = check_connectivity(E[i:j],len(G),0)
        if weight is not None:
            return weight
        i+=1
        j+=1

    return None
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )