from kol3btesty import runtests
import heapq
def airports( G, A, s, t ):
    new_graph = [[] for _ in range(len(G)+1)]
    for u in range(len(G)):
        for v,w in G[u]:
            new_graph[u].append((v,w))
            new_graph[v].append((u,w))
        new_graph[u].append((len(G),A[u]))
        new_graph[len(G)].append((u,A[u]))
    V = len(new_graph)
    pq = [(0,s)]
    dist = [float("inf") for _ in range(V)]
    dist[s] = 0

    while pq:
        curr_dist, u  = heapq.heappop(pq)
        if curr_dist > dist[u]:
            continue
        for v,w in new_graph[u]:
            if curr_dist+w < dist[v]:
                dist[v] = curr_dist + w
                heapq.heappush(pq,(dist[v],v))
    
    # tu prosze wpisac wlasna implementacje
    return dist[t]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )