'''
Najkrótsza ściezka w DAG 
'''

def topsort(G):
    q=[] # zamienić liste na queue zeby obnizyc time complexity
    q.append(0)
    n = len(G)
    sorted=[]
    visited=[False for _ in range(n)]
    while q:
        v=q.pop();
        for nb,weight in G[v]:
            if not visited[nb]:
                q.append(nb)
                visited[nb]=True
        sorted.append(v)

    return sorted

def shortest_path(G,s):
    sorted = topsort(G)
    d = [None for _ in range(len(G))]
    d[s] = 0
    for i in range(len(G)):
        v = sorted[i]
        for u,weight in G[v]:
            d[u] = min(d[v],d[u]+weight)
    return d



        
