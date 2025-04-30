'''
Alg. Dijkstry, repr listowa O(EVlogV)
'''
import heapq
def dijkstra(G,s):
    V = len(G)
    d = [float("inf") for _ in range(V)];
    parent = [None for _ in range(V)]
    d[s]=0
    Q=[(d[s],s)]
    while Q:
        dist,u = heapq.heappop(Q)
        if dist > d[u]:
            continue
        for v in range(V):
            if G[u][v]!=0 and d[v]>d[u]+G[u][v]:
                d[v] = d[u] + G[u][v]
                parent[v]=u
                heapq.heappush(Q,(d[v],v))
    
    return d,parent

