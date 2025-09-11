from kol3atesty import runtests
import heapq
def spacetravel( n, E, S, a, b ):
    graph = [[] for _ in range(n+1)]
    for u,v,w in E:
        graph[u].append((v,w))
        graph[v].append((u,w))

    for u in S:
        graph[n].append((u,0))
        graph[u].append((n,0))

    dist = [float("inf") for _ in range(n+1)]
    dist[a] = 0
    pq = [(0,a)]

    while pq:
        curr_dist,u = heapq.heappop(pq)
        if curr_dist > dist[u]:
            continue
        for v,w in graph[u]:
            if curr_dist + w < dist[v]:
                dist[v] = curr_dist + w
                heapq.heappush(pq,(dist[v], v))

    return dist[b] if dist[b] != float("inf") else None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )